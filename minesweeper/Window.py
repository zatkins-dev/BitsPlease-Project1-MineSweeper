import pygame
from pygame.locals import *
import math

class Window:
	def __init__(self, x_dim, y_dim):
		self.x_dim = x_dim
		self.y_dim = y_dim
		self.SPACE_PIXELS = 32
		self.MARGIN = 8
		self.HEADER_BAR = self.SPACE_PIXELS * 3
		self.WIDTH = self.SPACE_PIXELS*x_dim + 2 * self.MARGIN
		self.HEIGHT = self.SPACE_PIXELS*y_dim + 2 * self.MARGIN + self.HEADER_BAR

		pygame.init()
		pygame.font.init()
		self._screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
		self._gameScreen = self._screen.subsurface(Rect(self.MARGIN, self.HEADER_BAR + self.MARGIN, self.SPACE_PIXELS*x_dim, self.SPACE_PIXELS*y_dim))
		self._screen.fill(Color('light grey'))
		self._gameScreen.fill(Color('black'))

		pygame.display.set_caption("BitSweeper")
		self.clock = pygame.time.Clock()

	@property
	def gameScreen(self):
		return self._gameScreen

	@gameScreen.setter
	def setGameScreen(self, appSurface):
		""" Adds appSurface as a subsurface to screen """
		self._screen.subsurface(appSurface)

	def onClick(self, event):
		pos = event.pos
		print(pos)
		realPos = (math.floor((pos[0]-self.MARGIN)/self.SPACE_PIXELS), math.floor((pos[1]-self.MARGIN-self.HEADER_BAR)/self.SPACE_PIXELS))
		if not (0 <= realPos[0] <= self.x_dim-1 and 0 <= realPos[1] <= self.y_dim-1): 
			return True
		print (realPos)
		return pygame.event.Event(pygame.MOUSEBUTTONDOWN, {'pos': realPos, 'button': event.button})
		