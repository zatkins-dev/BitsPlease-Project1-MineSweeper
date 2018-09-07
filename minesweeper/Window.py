import pygame
from pygame.locals import *

class Window:
	def __init__(self, x_dim, y_dim):
		self.SPACE_PIXELS = 32
		self.MARGIN = self.SPACE_PIXELS / 4
		self.HEADER_BAR = self.SPACE_PIXELS * 3
		self.WIDTH = self.SPACE_PIXELS*x_dim + 2 * self.MARGIN
		self.HEIGHT = self.SPACE_PIXELS*y_dim + 2 * self.MARGIN + self.HEADER_BAR

		pygame.init()
		pygame.font.init()
		self._screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
		self._gameScreen = self._screen.subsurface(Rect(self.MARGIN, self.HEADER_BAR + self.MARGIN, self.SPACE_PIXELS*x_dim, self.SPACE_PIXELS*y_dim))
		self._screen.fill(Color('light grey'))
		self._gameScreen.fill(Color('black'))

	@property
	def gameScreen(self):
		return self._gameScreen

	@gameScreen.setter
	def setGameScreen(self, appSurface):
		""" Adds appSurface as a subsurface to screen """
		self._screen.subsurface(appSurface)


