
import pygame
from pygame.locals import *
from Minefield import *
from Window import Window
import os
import math

class App:
	def __init__(self):
		self.x_dim = 20
		self.y_dim = 10
		self.n_mines = 10

		self.flagCounter = self.n_mines

		self.SPACE_WIDTH = 32
		self.SPACE_HEIGHT = 32
		self.WIDTH = self.SPACE_WIDTH*self.x_dim
		self.HEIGHT = self.SPACE_HEIGHT*self.y_dim

		self.minefield = Minefield(self.x_dim, self.y_dim, self.n_mines)
		self.grid = self.minefield.minefield

		self.window = Window(self.x_dim, self.y_dim)
		self.screen = self.window.gameScreen
		#Images
		self.imageRevealed = pygame.image.load('./assets/space_empty_green.png').convert()
		self.imageUnrevealed = pygame.image.load("./assets/gridSpace.png").convert()
		self.imageFlag = pygame.image.load("./assets/gridSpaceFlag.png").convert()
		self.imageMine = pygame.image.load("./assets/space_empty_rose-gold.png").convert()
		
	def onClick(self, event):
		newEvent = self.window.onClick(event)
		if newEvent == True:
			return 
		print(newEvent.pos)
		activeSpace = self.minefield.getSpace(newEvent.pos[0],newEvent.pos[1])
		if activeSpace.isRevealed:
			pass
		elif event.button == 1:
			if self.minefield.reveal(newEvent.pos[0],newEvent.pos[1]):
				self.render()
				return True
		elif event.button == 3:
			if not activeSpace.isRevealed:
				if not activeSpace.isFlagged:
					self.flagCounter = self.flagCounter - 1
					if self.flagCounter == 0:
						if self.minefield.checkFlags:
							#TODO: what happens when they win?
							print('checked flags - true')
							pygame.quit()
						else:
							print('checked flags - false')
							pass
							# do nothing
				else:
					self.flagCounter = self.flagCounter + 1
				self.minefield.toggleFlag(newEvent.pos[0],newEvent.pos[1])
		return False

	def render(self):
		for y in range(self.minefield.y_size):
			for space in self.grid[y]:
				self.renderSpace(space)
		pygame.display.flip()

	def renderSpace(self, space):
		image = self.imageUnrevealed
		if space.isRevealed:
			if space.isMine:
				image = self.imageMine
			else:
				image = self.imageRevealed
		elif space.isFlagged:
			image = self.imageFlag
		self.screen.blit(image, (space.x_loc*self.window.SPACE_PIXELS, space.y_loc*self.window.SPACE_PIXELS))
		#pygame.draw.rect(self.screen, color, Rect(space.x_loc*self.SPACE_WIDTH, space.y_loc*self.SPACE_HEIGHT, self.SPACE_WIDTH, self.SPACE_HEIGHT))

		if space.isRevealed:
			if not space.numOfSurroundingMines or space.isMine:
				return
			font = pygame.font.SysFont('comicsansms', 20)
			text = font.render(str(space.numOfSurroundingMines), True, (0,0,0))
			x_text_pos = (space.x_loc * self.window.SPACE_PIXELS) + (self.window.SPACE_PIXELS / 2) - (text.get_width() / 2)
			y_text_pos = (space.y_loc * self.window.SPACE_PIXELS) + (self.window.SPACE_PIXELS / 2) - (text.get_height() / 2)
			self.screen.blit(text, (x_text_pos, y_text_pos))

	def reset(self):
		self.minefield = Minefield(self.x_dim, self.y_dim, self.n_mines)
		self.flagCounter = self.n_mines

    
	def getTime(self):
		return pygame.time.get_ticks / 1000


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

		app.window.clock.tick(60)
	
	pygame.quit()

if __name__ == '__main__': main()

		

