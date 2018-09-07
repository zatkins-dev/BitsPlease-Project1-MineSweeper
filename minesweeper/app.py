
import pygame
from pygame.locals import *
from Minefield import *
import math

class App:
	def __init__(self):
		x_dim = 20
		y_dim = 10
		n_mines = 10

		self.flagCounter = n_mines

		self.SPACE_WIDTH = 32
		self.SPACE_HEIGHT = 32
		self.WIDTH = self.SPACE_WIDTH*x_dim
		self.HEIGHT = self.SPACE_HEIGHT*y_dim

		self.minefield = Minefield(x_dim, y_dim, n_mines)
		self.grid = self.minefield.minefield

		#Images
		self.imageRevealed = pygame.image.load("..\\assets\\gridSpace_revealed.png")
		self.imageUnrevealed = pygame.image.load("..\\assets\\gridSpace.png")
		self.imageFlag = pygame.image.load("..\\assets\\flag.png")
		self.imageMine = pygame.image.load("..\\assets\\mine.png")

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
				if not activeSpace.isFlagged:
					self.flagCounter = self.flagCounter - 1
					if self.flagCounter == 0:
						isDone = self.minefield.checkFlags
						if isDone == True:
							#TODO: what happens when they win?
							pygame.quit()
						else:
							pass
							# do nothing
				else:
					self.flagCounter = self.flagCounter + 1
				self.minefield.toggleFlag(realPos[0],realPos[1])
		return False

	def render(self):
		for y in range(self.minefield.y_size):
			for space in self.grid[y]:
				self.renderSpace(space)
		pygame.display.flip()

	def renderSpace(self, space):
		space_x = space.x_loc*self.SPACE_WIDTH
		space_y = space.y_loc*self.SPACE_HEIGHT

		#Draw revealed space background
		if space.isRevealed:
			self.screen.blit(self.imageRevealed, (space_x, space_y))
			#Draw either a mine, or text ontop of background
			if space.isMine:
				self.screen.blit(self.imageMine, (space_x, space_y))
			elif space.numOfSurroundingMines != 0:
				#Draw Text
				font = pygame.font.SysFont('lucidaconsole', 20)
				text = font.render(str(space.numOfSurroundingMines), True, (0,0,0))
				x_text_pos = (space.x_loc * self.SPACE_WIDTH) + (self.SPACE_WIDTH / 2) - (text.get_width() / 2)
				y_text_pos = (space.y_loc * self.SPACE_HEIGHT) + (self.SPACE_HEIGHT / 2) - (text.get_height() / 2)
				self.screen.blit(text, (x_text_pos, y_text_pos))
		else:
			self.screen.blit(self.imageUnrevealed, (space_x, space_y))
			#Draw a flag if the space is flagged
			if space.isFlagged:
				self.screen.blit(self.imageFlag, (space_x, space_y))	

	def reset():
		self.minefield = Minefield(x_dim, y_dim, n_mines)
		self.flagCounter = n_mines

    
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

		app.clock.tick(60)
	
	pygame.quit()

if __name__ == '__main__': main()

		

