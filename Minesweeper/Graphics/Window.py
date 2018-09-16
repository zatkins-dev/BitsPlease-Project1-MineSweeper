from pygame import font, display, time, event, constants, init
from pygame.locals import Rect, Color
import math

class Window:
	def __init__(self, x_dim, y_dim):
		self.x_dim = x_dim
		self.y_dim = y_dim
		self.SPACE_PIXELS = 32
		self.MARGIN = 8
		if (math.floor(self.SPACE_PIXELS * self.y_dim/4)) < 70 :
			self.HEADER_BAR = 70
		else:
			self.HEADER_BAR = math.floor(self.SPACE_PIXELS * self.y_dim/4)
		if (self.SPACE_PIXELS*x_dim + 2 * self.MARGIN) < 300 :
			self.WIDTH = 300
		else: 
			self.WIDTH = self.SPACE_PIXELS*x_dim + 2 * self.MARGIN
		self.HEIGHT = self.SPACE_PIXELS*y_dim + 2 * self.MARGIN + self.HEADER_BAR
		self.RESET_WIDTH = math.floor(self.WIDTH/3)
		self.TIMER_WIDTH = 150
		self.FLAG_COUNTER_HEIGHT = 20
		self.FLAG_COUNTER_WIDTH = 150
		init()
		self._screen = display.set_mode((self.WIDTH, self.HEIGHT))
		if (self.x_dim*self.SPACE_PIXELS) < self.WIDTH :
			self.GAME_SCREEN_LEFT = (self.WIDTH / 2) - ((self.x_dim* self.SPACE_PIXELS) / 2)
		else :
			self.GAME_SCREEN_LEFT = self.MARGIN
		self._gameScreen = self._screen.subsurface(Rect(self.GAME_SCREEN_LEFT, self.HEADER_BAR + self.MARGIN, self.SPACE_PIXELS*x_dim, self.SPACE_PIXELS*y_dim))
		self._reset = self._screen.subsurface(Rect(self.MARGIN, self.MARGIN, self.RESET_WIDTH, self.HEADER_BAR-self.MARGIN))
		self._timer = self._screen.subsurface(Rect(self.MARGIN + self.RESET_WIDTH + self.MARGIN, self.MARGIN, self.TIMER_WIDTH, self.FLAG_COUNTER_HEIGHT))
		self._flagCounter = self._screen.subsurface(Rect(self.MARGIN + self.RESET_WIDTH + self.MARGIN, self.MARGIN + self.FLAG_COUNTER_HEIGHT, self.FLAG_COUNTER_WIDTH, self.FLAG_COUNTER_HEIGHT))
		self._screen.fill(Color('light grey'))
		self._gameScreen.fill(Color('black'))

		display.flip()

		display.set_caption("BitSweeper")
		self.clock = time.Clock()

	def onClick(self, newEvent):
		"""
		On click handler for window
		
		**Args**:
				*newEvent*: pygame Event object, newEvent.pos: pixel location of click, newEvent.button: mouse button clicked
		
		**Preconditions**:
				None.
		
		**Postconditions**:
				None.
		
		**Returns**:
				pygame Event object, with same button and gid location if on grid, else button=-1 if on reset button, else None
		"""
		x,y = newEvent.pos
		x_game, y_game = (math.floor((x-self.GAME_SCREEN_LEFT)/self.SPACE_PIXELS), math.floor((y-self.MARGIN-self.HEADER_BAR)/self.SPACE_PIXELS))
		if not (0 <= x_game <= self.x_dim-1 and 0 <= y_game <= self.y_dim-1): 
			x_min,y_min = self._reset.get_abs_offset()
			x_reset_size, y_reset_size = self._reset.get_size()
			(x_max, y_max) = (x_min + x_reset_size, y_min + y_reset_size) 
			if (x_min <= x <= x_max) and (y_min <= y <= y_max):
				return event.Event(constants.MOUSEBUTTONDOWN, {'pos': newEvent.pos, 'button': -1})
			return None
		return event.Event(constants.MOUSEBUTTONDOWN, {'pos': (x_game, y_game), 'button': newEvent.button})
