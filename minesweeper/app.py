#!/usr/local/bin/python3
import pygame
from pygame.locals import *
from Minefield import *
import math

class App:
	def __init__(self):
		x_dim = 5
		y_dim = 5
		n_mines = 2

		self.SPACE_WIDTH = 32
		self.SPACE_HEIGHT = 32
		self.WIDTH = self.SPACE_WIDTH*x_dim
		self.HEIGHT = self.SPACE_HEIGHT*y_dim

		self.minefield = Minefield(x_dim, y_dim, n_mines)
		self.grid = self.minefield.minefield

		pygame.init()
		self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
		self.screen.fill(Color('black'))

		pygame.display.set_caption("BitSweeper")
		self.clock = pygame.time.Clock()
		
	def onClick(self, event):
		pos = event.pos
		realPos = (math.floor(pos[0]/self.SPACE_WIDTH), math.floor(pos[1]/self.SPACE_HEIGHT))
		print(realPos)
		activeSpace = self.minefield.getSpace(realPos[0],realPos[1])
		if activeSpace.isRevealed:
			pass
		elif event.button == 1:
			if self.minefield.reveal(realPos[0],realPos[1]):
				self.screen.fill(Color('red'))
		elif event.button == 3:
			if not activeSpace.isFlagged:
				self.minefield.toggleFlag(realPos[0],realPos[1])

	def render(self):
		for y in range(self.minefield.y_size):
			for space in self.grid[y]:
				color = Color('black')
				if space.isRevealed:
					if space.isMine:
						color = Color('red')
					else:
						color = Color('grey')
				elif space.isFlagged:
					color = Color('blue')
				pygame.draw.rect(self.screen, color, Rect(space.x_loc*self.SPACE_WIDTH, space.y_loc*self.SPACE_HEIGHT, self.SPACE_WIDTH, self.SPACE_HEIGHT))
		pygame.display.flip()

def main():	
	app = App()

	exit = False
	while not exit:
		for event in pygame.event.get():
			# Quit Event 
			if event.type == pygame.QUIT:
				exit = True
			elif event.type == pygame.MOUSEBUTTONDOWN:
				app.onClick(event)

		app.render()

		app.clock.tick(60)
	
	pygame.quit()

if __name__ == '__main__': main()

		

