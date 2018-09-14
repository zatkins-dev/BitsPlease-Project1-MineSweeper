import pygame
from pygame.locals import *
from Minesweeper.Graphics.Drawer import Drawer
class StartScreen:
	def __init__(self):
		pygame.init()
		self.x_size = 9
		self.y_size = 9
		self.numMines = 10
		self.window_x_size = 600
		self.window_y_size = 500
		self.window_margin = 20
		self.window = pygame.display.set_mode((self.window_x_size, self.window_y_size))
		
		self.sizeSurface = self.window.subsurface(Rect(self.window_margin, self.window_margin, self.window_x_size / 2 - 1.5*self.window_margin - 1, self.window_y_size - 2 * self.window_margin - 100))
		
		self.mineSurface = self.window.subsurface(Rect((self.window_x_size / 2) + .5*self.window_margin, self.window_margin, self.window_x_size / 2 - 1.5*self.window_margin, self.window_y_size - 2 * self.window_margin - 100))
		
		self.startSurface = self.window.subsurface(Rect(self.window_margin, 400, self.window_x_size - 2*self.window_margin, 100 - self.window_margin))
		
		self.window.fill(Color('light grey'))
		self.sizeSurface.fill(Color('dark grey'))
		self.mineSurface.fill(Color('dark gray'))
		self.clock = pygame.time.Clock()
		self.title = pygame.font.SysFont('lucidaconsole', 30)
		self.subtitle = pygame.font.SysFont('lucidaconsole', 25)

		self.drawer = Drawer()
		self.drawButton = self.drawer.drawButton

		self.gameReady = False

	def render(self):
		#render texts for the labels
		sizeLabel = self.title.render("Size:", True, Color('black'))
		sizeLabel_x = self.subtitle.render("Width:", True, Color('black'))
		sizeLabel_y = self.subtitle.render("Height:", True, Color('black'))
		mineLabel = self.title.render("Mines:", True, Color('black'))

		currSize_x = self.subtitle.render(str(self.x_size), True, Color('white'))
		currSize_y = self.subtitle.render(str(self.y_size), True, Color('white'))
		currMines = self.subtitle.render(str(self.numMines), True, Color('white'))

		#find the positions of these labels
		sizeLabelPos = (self.sizeSurface.get_width() / 2 - sizeLabel.get_width() / 2, 20)
		sizeLabelPos_x = (self.sizeSurface.get_width() / 4 - sizeLabel.get_width() / 2, 60)
		sizeLabelPos_y = (3 * self.sizeSurface.get_width() / 4 - sizeLabel.get_width() / 2, 60)
		mineLabelPos = (self.mineSurface.get_width() / 2 - mineLabel.get_width() / 2, 30)

		#define common vars for the buttons
		buttonWidth_x = sizeLabel_x.get_width()
		buttonWidth_mine = mineLabel.get_width()
		buttonLeft_x = sizeLabelPos_x[0]
		buttonLeft_y = sizeLabelPos_y[0]
		buttonLeft_mine = mineLabelPos[0]
		buttonTop = sizeLabelPos_x[1] + sizeLabel_x.get_height() + 20 

		buttonHeight = 60

		buttonColor = (128,128,128)
		buttonHoverColor = (96,96,96)

		startButtonColor = (0, 180, 0)
		startButtonHoverColor = (0, 156, 0)

		self.drawButton(self.sizeSurface, buttonLeft_x, buttonTop, buttonWidth_x, buttonHeight, buttonColor, buttonHoverColor, "+", 25, self.incWidth)
		self.drawButton(self.sizeSurface, buttonLeft_x, buttonTop + buttonHeight * 2, buttonWidth_x, buttonHeight, buttonColor, buttonHoverColor, "-", 25, self.decWidth)
		self.drawButton(self.sizeSurface, buttonLeft_y, buttonTop, buttonWidth_x, buttonHeight, buttonColor, buttonHoverColor, "+", 25, self.incHeight)
		self.drawButton(self.sizeSurface, buttonLeft_y, buttonTop + buttonHeight * 2, buttonWidth_x, buttonHeight, buttonColor, buttonHoverColor, "-", 25, self.decHeight)

		self.drawButton(self.mineSurface, buttonLeft_mine, buttonTop, buttonWidth_mine, buttonHeight, buttonColor, buttonHoverColor, "+", 25, self.incMines)
		self.drawButton(self.mineSurface, buttonLeft_mine, buttonTop + buttonHeight * 2, buttonWidth_mine, buttonHeight, buttonColor, buttonHoverColor, "-", 25, self.decMines)

		self.drawButton(self.startSurface, 0, 0, self.startSurface.get_width(), self.startSurface.get_height(), startButtonColor, startButtonHoverColor, "Start!", 30, self.start)

		pygame.draw.rect(self.sizeSurface, Color('black'), (buttonLeft_x, buttonTop + buttonHeight, buttonWidth_x, buttonHeight))
		pygame.draw.rect(self.sizeSurface, Color('black'), (buttonLeft_y, buttonTop + buttonHeight, buttonWidth_x, buttonHeight))
		pygame.draw.rect(self.mineSurface, Color('black'), (buttonLeft_mine, buttonTop + buttonHeight, buttonWidth_mine, buttonHeight))

		currSizePos_x = (self.sizeSurface.get_width() / 4 - currSize_x.get_width() / 2, buttonTop + buttonHeight * 1.5 - currSize_x.get_height() / 2)
		currSizePos_y = (3 * self.sizeSurface.get_width() / 4 - currSize_y.get_width() / 2, buttonTop + buttonHeight * 1.5 - currSize_y.get_height() / 2)
		currMinesPos = (self.mineSurface.get_width() / 2 - currMines.get_width() / 2, buttonTop + buttonHeight * 1.5 - currMines.get_height() / 2)

		#draw the labels to the screen
		self.sizeSurface.blits([
			(sizeLabel, sizeLabelPos),
			(sizeLabel_x, sizeLabelPos_x),
			(sizeLabel_y, sizeLabelPos_y),
			(currSize_x, currSizePos_x),
			(currSize_y, currSizePos_y)
		])
		self.mineSurface.blits([
			(mineLabel, mineLabelPos),
			(currMines, currMinesPos)
		])
		

		pygame.display.flip()

	def incWidth(self):
		self.x_size += 1

	def decWidth(self):
		if self.x_size > 5:
			self.x_size -= 1
		if self.numMines >= self.x_size * self.y_size:
			self.numMines = self.x_size * self.y_size - 1

	def incHeight(self):
		self.y_size += 1

	def decHeight(self):
		if self.y_size > 5:
			self.y_size -= 1
		if self.numMines >= self.x_size * self.y_size:
			self.numMines = self.x_size * self.y_size - 1

	def incMines(self):
		if self.numMines < self.x_size * self.y_size - 1:
			self.numMines += 1
	
	def decMines(self):
		if self.numMines > 1:
			self.numMines -= 1

	def start(self):
		self.gameReady = True