from pygame import surface, display, constants
from pygame.font import SysFont
from pygame.locals import Color

class EndScreen:
	"""EndScreen manages post game conditions, tells the user whether they won or lost, and will restart the game.
	The win state is passed in at construction time via the gameWon boolean parameter.
	
	**Class Variables**:
		*gameSurf*: Surface A copy of the game screen to be used as a base for other transparent drawing

		*drawWindow*: Surface The active game surface to draw to

		*transparentSurf*: Surface A transparent surface to draw. Will be green on a win, and red on a loss.

		*titleSurf*: Surface A rendering of more emphasized text, such as "You Won!"

		*subtitleSurf*: Surface A rendering of less emphasized text, such as "Click to play again..."

		*textBackgroundSurf*: Surface A background to put behind the rendered text

		*titlePos*: Tuple (Int, Int) Holds the (x,y) corrdinates of the title surface

		*subtitlePos*: Tuple (Int, Int) Holds the (x,y) coordinates of the subtitle surface

		*textBackgroundPos*: Tuple (Int, Int) Holds the (x,y) coordinates of the text's background
	"""
	def __init__(self, gameWon):
		self.gameSurf = display.get_surface().copy()
		self.drawWindow = display.get_surface()
		self.transparentSurf = surface.Surface(display.get_surface().get_size(), constants.SRCALPHA)

		color = (0,255, 0, 127) if gameWon else (255, 0, 0, 127)
		text = "You Won!" if gameWon else "You Lost..."
		backgroundColor = (0,255,0) if gameWon else (255,0,0)
		title = SysFont('lucidaconsole', 25)
		subtitle = SysFont('lucidaconsole', 15)

		#distance between title and subtitle text
		textMargin = 10
		#distance between edge of text and full opacity background
		textBackgroundMargin = 10

		self.transparentSurf.fill(color)
		self.titleSurf = title.render(text, True, Color('black'))
		self.subtitleSurf = subtitle.render("Click to play again", True, Color('black'))

		self.textBackgroundSurf = surface.Surface(
			(self.subtitleSurf.get_width() + 2*textBackgroundMargin),
			(self.titleSurf.get_height() + self.subtitleSurf.get_height() + textMargin + 2*textBackgroundMargin)
		)

		self.textBackgroundSurf.fill(backgroundColor)

		self.titlePos = (
			self.drawWindow.get_width() / 2 - self.titleSurf.get_width() / 2,
			self.drawWindow.get_height() / 2 - self.titleSurf.get_height() - textMargin / 2
		)
		self.subtitlePos = (
			self.drawWindow.get_width() / 2 - self.subtitleSurf.get_width() / 2, 
			self.drawWindow.get_height() / 2 + textMargin / 2
		)
		self.textBackgroundPos = (
			self.drawWindow.get_width() / 2 - self.textBackgroundSurf.get_width() / 2,
			self.drawWindow.get_height() / 2 - self.textBackgroundSurf.get_height() / 2
		)

	def render(self):
		"""
		Renders the ending screen. This includes message text and a transparent color 
		
		**Args**:
				None.
		
		**Preconditions**:
				None.
		
		**Postconditions**:
				EndScreen's contents will be rendered to the main pygame display surface.
		
		**Returns**:
				None.
		"""
		self.drawWindow.blit(self.gameSurf, (0,0))
		self.drawWindow.blit(self.transparentSurf, (0,0), None, constants.BLEND_RGBA_MULT)
		self.drawWindow.blits([
			(self.textBackgroundSurf, self.textBackgroundPos),
			(self.titleSurf, self.titlePos),
			(self.subtitleSurf, self.subtitlePos)
		])

		display.flip()	