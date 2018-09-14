
import pygame
from pygame.locals import *
from Minesweeper.Minefield import Minefield
from Minesweeper.Graphics.Window import Window
from Minesweeper.StartScreen import StartScreen
from Minesweeper.Graphics.Drawer import Drawer
import os
import math

class App:
	def __init__(self, x=9, y=9, mines=10):
		self.x_dim = x
		self.y_dim = y
		self.n_mines = mines

		self.flagCounter = self.n_mines
		self.gameTimer = 0
		self.timeOfLastTimeUpdate = 0
		self.timeOfLastReset = pygame.time.get_ticks()

		self.SPACE_WIDTH = 32
		self.SPACE_HEIGHT = 32
		self.WIDTH = self.SPACE_WIDTH*self.x_dim
		self.HEIGHT = self.SPACE_HEIGHT*self.y_dim

		self.drawer = Drawer()
		self.drawButton = self.drawer.drawButton

		self.minefield = Minefield(self.x_dim, self.y_dim, self.n_mines)
		self.grid = self.minefield.minefield

		self.window = Window(self.x_dim, self.y_dim)
		self.screen = self.window.gameScreen
		self.reset_element = self.window._reset
		self.timer_element = self.window._timer
		#Images
		self.imageRevealed = pygame.image.load('Minesweeper/assets/gridSpace_revealed.png').convert()
		self.imageUnrevealed = pygame.image.load("Minesweeper/assets/gridSpace.png").convert()
		self.imageFlag = pygame.image.load("Minesweeper/assets/flag.png").convert_alpha()
		self.imageMine = pygame.image.load("Minesweeper/assets/mine.png").convert_alpha()

		
		
	def onClick(self, event):
		newEvent = self.window.onClick(event)
		(gameOver, win) = False, False
		if newEvent == 'RESET':
			gameOver = True
			return gameOver, newEvent
		if not newEvent:
			return gameOver, newEvent
		activeSpace = self.minefield.getSpace(newEvent.pos[0],newEvent.pos[1])
		if activeSpace.isRevealed:
			pass
		elif event.button == 1:
			if self.minefield.reveal(newEvent.pos[0],newEvent.pos[1]):
				self.render()
				gameOver = True
				return gameOver, win
		elif event.button == 3:
			if not activeSpace.isRevealed:
				if not activeSpace.isFlagged:
					if self.flagCounter == 0:
						return gameOver, win
					self.flagCounter = self.flagCounter - 1
					self.minefield.toggleFlag(newEvent.pos[0],newEvent.pos[1])
					if self.flagCounter == 0:
						isDone = self.minefield.checkFlags()
						if isDone == True:
							gameOver = True
							win = True
							return gameOver, win
						else:
							pass
							# do nothing
				else:
					self.flagCounter = self.flagCounter + 1
					self.minefield.toggleFlag(newEvent.pos[0],newEvent.pos[1])
				
		return gameOver, win

	def render(self):
		for y in range(self.minefield.y_size):
			for space in self.grid[y]:
				self.renderSpace(space)

		reset_text = 'Reset'
		(reset_left, reset_top) = self.reset_element.get_abs_offset()
		(reset_x, reset_y) = self.reset_element.get_size()
		reset_fontsize = 20
		t_font = pygame.font.SysFont('lucidaconsole', reset_fontsize)
		while t_font.size(reset_text)[0] > reset_y + 4:
			reset_fontsize -= 1
			t_font = pygame.font.SysFont('lucidaconsole', reset_fontsize)
		self.drawButton(self.window._screen, reset_left, reset_top, reset_x, reset_y, pygame.Color('magenta'), pygame.Color('red'), reset_text, reset_fontsize, self.reset)
		self.updateClock()
		# self.reset_element.fill(pygame.Color('magenta'))
		# reset_text_ln1 = pygame.font.SysFont('lucidiaconsole', reset_fontsize).render('Reset', True, (0,0,0))
		# reset_text_ln2 = pygame.font.SysFont('lucidiaconsole', reset_fontsize).render('Game', True, (0,0,0))
		# reset_text_pos = tuple(map(lambda x, y, z: x + y - z, self.reset_element.get_abs_offset(), map(lambda x: x/2,self.reset_element.get_size()), map(lambda x: x/2, reset_text_ln1.get_size())))
		# self.reset_element.blit(reset_text_ln1, reset_text_pos)
		# self.reset_element.blit(reset_text_ln2, (reset_text_pos[0], reset_text_pos[1]+reset_fontsize+2))
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
				x_text_pos = (space_x) + (self.SPACE_WIDTH / 2) - (text.get_width() / 2)
				y_text_pos = (space_y) + (self.SPACE_HEIGHT / 2) - (text.get_height() / 2)
				self.screen.blit(text, (x_text_pos, y_text_pos))
		else:
			self.screen.blit(self.imageUnrevealed, (space_x, space_y))
			#Draw a flag if the space is flagged
			if space.isFlagged:
				self.screen.blit(self.imageFlag, (space_x, space_y))	

	def reset(self):
		self.minefield = Minefield(self.x_dim, self.y_dim, self.n_mines)
		self.flagCounter = self.n_mines
		self.timeOfLastReset = pygame.time.get_ticks()
	

	def getTime(self):
		return int((pygame.time.get_ticks() - self.timeOfLastReset) / 1000)
	
	#Not correctly working yet, but functional.
	def updateClock(self):
		font = pygame.font.SysFont('lucidaconsole', 20)
		
		text = font.render("Time: " + str(self.getTime()), False, (0,0,0))
		#This needs to be positioned in the header!
		self.timer_element.fill(Color('light grey'))
		self.timer_element.blit(text, (0,0))	
		pygame.display.flip() 
		



def main():	
	exit = False
	while not exit:
	
		startScreen = StartScreen()
		gameStarting = True
		while gameStarting and not exit:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit = True
			startScreen.render()
			gameStarting = not startScreen.gameReady
			startScreen.clock.tick(60)
			
		
		app = App(startScreen.x_size, startScreen.y_size, startScreen.numMines)
		gameRunning = True
		while gameRunning and not exit:
			for event in pygame.event.get():
				# Quit Event 
				if event.type == pygame.QUIT:
					pygame.quit()
				elif event.type == pygame.MOUSEBUTTONDOWN:
					(end, win) = app.onClick(event)
					if end:
						#app.window.gameScreen.lock()
						# TODO: Game over screen
						if win == 'RESET':
							gameRunning = False
						elif win:
							print('Winner!!')
							# TODO: Win screen
							gameRunning = False
						else:
							print('Loser.')
							# TODO: Lose screen/ bomb cascade
							gameRunning = False
						#app.window.gameScreen.unlock()
			app.render()
			app.window.clock.tick(60)
	pygame.quit()

	