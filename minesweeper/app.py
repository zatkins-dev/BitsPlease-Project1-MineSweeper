#!/usr/local/bin/python3
import pygame
from pygame.locals import *
from Minefield import *
import math

class App:
	def __init__(self):
		x_dim = 20
		y_dim = 10
		n_mines = 10

		self.SPACE_WIDTH = 32
		self.SPACE_HEIGHT = 32
		self.WIDTH = self.SPACE_WIDTH*x_dim
		self.HEIGHT = self.SPACE_HEIGHT*y_dim

		self.minefield = Minefield(x_dim, y_dim, n_mines)
		self.grid = self.minefield.minefield

		pygame.init()
		pygame.font.init()
		self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
		self.screen.fill(Color('black'))

		pygame.display.set_caption("BitSweeper")
		self.clock = pygame.time.Clock()
		
	def onClick(self, event):
		pos = event.pos
		realPos = (math.floor(pos[0]/self.SPACE_WIDTH), math.floor(pos[1]/self.SPACE_HEIGHT))
		activeSpace = self.minefield.getSpace(realPos[0],realPos[1])
		if activeSpace.isRevealed:
			pass
		elif event.button == 1:
			if self.minefield.reveal(realPos[0],realPos[1]):
				self.render()
				return True
		elif event.button == 3:
			if not activeSpace.isRevealed:
				self.minefield.toggleFlag(realPos[0],realPos[1])
		return False

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

				if space.isRevealed:
					if not space.numOfSurroundingMines or space.isMine:
						continue
					font = pygame.font.SysFont('comicsansms', 20)
					text = font.render(str(space.numOfSurroundingMines), True, (0,0,0))
					x_text_pos = (space.x_loc * self.SPACE_WIDTH) + (self.SPACE_WIDTH / 2) - (text.get_width() / 2)
					y_text_pos = (space.y_loc * self.SPACE_HEIGHT) + (self.SPACE_HEIGHT / 2) - (text.get_height() / 2)
					self.screen.blit(text, (x_text_pos, y_text_pos))
		pygame.display.flip()

def main():	
	app = App()

	exit = False
	rerender = True
	while not exit:
		for event in pygame.event.get():
			# Quit Event 
			if event.type == pygame.QUIT:
				exit = True
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if app.onClick(event):
					rerender = False

		if rerender: app.render()

		app.clock.tick(60)
	
	pygame.quit()

if __name__ == '__main__': main()

		

