import pygame
from pygame.locals import *

class Window:
	def __init__(self, x_dim, y_dim):
		self.SPACE_PIXELS = 32
		self.MARGIN = self.SPACE_PIXELS/4
		self.WIDTH = self.SPACE_PIXELS*x_dim + 2 * self.MARGIN
		self.HEIGHT = self.SPACE_PIXELS*y_dim + 2 * self.MARGIN

		pygame.init()
		pygame.font.init()
		self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
		self.screen.fill(Color('light grey'))

		



