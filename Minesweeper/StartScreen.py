from pygame import display, time, font, draw, init
from pygame.locals import Rect, Color
from Minesweeper.Graphics.Drawer import Drawer
class StartScreen:
	"""Minefield manages the internal game logic. The backend of the game board.
	
	Minefield is designed to be our internal game engine. In this class, there is logic to determine where the mines are placed, to reveal the gameboard, and deal with flags.
	
	**Class Variables**:
			*min_size*: Integer The minimum board size to be allowed by the game

			*max_y*: Integer The maximum board height to be allowed by the game

			*max_x*: Integer The maximum board width to be allowed by the game

			*x_size*: Integer Keeps track of the selected board width

			*y_size*: Integer Keeps track of the selected board height

			*numMines*: Integer The currently selected number of mines

			*window_x_size*: 

			*window_y_size*:

			*window_margin*:

			*window*:

			*sizeSurface*:

			*mineSurface*:

			*startSurface*:

			*title*:

			*subtitle*:	
	"""
	def __init__(self, x_size_init = 9, y_size_init = 9, numMines_init = 10):	
		init()

		#limits on board size selections
		self.min_size = 2
		self.max_y = 20
		self.max_x = 40

		#initialize member variables with initial values
		self.x_size = x_size_init
		self.y_size = y_size_init
		self.numMines = numMines_init

		#define a size for the menu window
		self.window_x_size = 600
		self.window_y_size = 500
		self.window = display.set_mode((self.window_x_size, self.window_y_size))
		
		self.window_margin = 20	
		self.sizeSurface = self.window.subsurface(Rect(self.window_margin, self.window_margin, self.window_x_size / 2 - 1.5*self.window_margin - 1, self.window_y_size - 2 * self.window_margin - 100))
		self.mineSurface = self.window.subsurface(Rect((self.window_x_size / 2) + .5*self.window_margin, self.window_margin, self.window_x_size / 2 - 1.5*self.window_margin, self.window_y_size - 2 * self.window_margin - 100))
		self.startSurface = self.window.subsurface(Rect(self.window_margin, 400, self.window_x_size - 2*self.window_margin, 100 - self.window_margin))
		
		self.window.fill(Color('light grey'))
		self.sizeSurface.fill(Color('dark grey'))
		self.mineSurface.fill(Color('dark gray'))

		self.title = font.SysFont('lucidaconsole', 30)
		self.subtitle = font.SysFont('lucidaconsole', 25)

		self.drawer = Drawer()
		self.drawButton = self.drawer.drawButton

		self.gameReady = False

	def render(self):
		"""
		Renders the minefield, reset button, flag counter, and timer
		
		**Args**:
				None.
		
		**Preconditions**:
				None.
		
		**Postconditions**:
				None.
		
		**Returns**:
				None.
		"""
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

		draw.rect(self.sizeSurface, Color('black'), (buttonLeft_x, buttonTop + buttonHeight, buttonWidth_x, buttonHeight))
		draw.rect(self.sizeSurface, Color('black'), (buttonLeft_y, buttonTop + buttonHeight, buttonWidth_x, buttonHeight))
		draw.rect(self.mineSurface, Color('black'), (buttonLeft_mine, buttonTop + buttonHeight, buttonWidth_mine, buttonHeight))

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
		

		display.flip()

	def incWidth(self):
		if self.x_size < self.max_x:
			self.x_size += 1

	def decWidth(self):
		if self.x_size > self.min_size:
			self.x_size -= 1
		if self.numMines >= self.x_size * self.y_size:
			self.numMines = self.x_size * self.y_size - 1

	def incHeight(self):
		if self.y_size < self.max_y:
			self.y_size += 1

	def decHeight(self):
		if self.y_size > self.min_size:
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