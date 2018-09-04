from Space import Space
import random

class Minefield:

	x_size = 0
	y_size = 0
	numMines = 0
	minefield = []

	def __init__(self, x_size, y_size, numMines):

		self.x_size = x_size
		self.y_size = y_size
		self.numMines = numMines

		#initialize minefield array
		self.minefield = [[Space(x,y) for x in range(x_size)] for y in range(y_size)]

		# for y in range(self.y_size):
		# 	self.minefield[y] = []
		# 	for x in range(self.x_size):
		# 		self.minefield[y][x] = Space(x, y)

		#set mines in the minefield
		self.setMines()

		#initialize surrounding mine numbers
		for y in range(self.y_size):
			for x in range(self.x_size):
				self.checkNeighbors(x, y)

	def setMines(self):

		currentMines = 0
		random.seed()

		while currentMines < self.numMines:
			mine_x, mine_y = random.randrange(self.x_size), random.randrange(self.y_size)
			thisSpace = self.getSpace(mine_x, mine_y)

			if not thisSpace.isMine:
				thisSpace.isMine = True
				currentMines += 1

	def checkNeighbors(self, x, y):
		"""Determines the number of mines that are directly around a certain space.
				
			Args:
				self: refers to the game board itself to access all the other spaces.
				x: the x coordinate of the space (start at 0)
				y: the y coordinate of the space (start at 0)
					
			Preconditions:
				The mines must already be placed in the grid, spaces must exist

			Postconditions:
				numOfSurroundingMines in space(x, y) will be altered to the number of surrounding mines.

			Returns:
				Sets the variable numOfSurroundingMines in the space in x,y to the integer number of mines touching that space."""
		#Using the count variable to monitor the number of surrounding mines 
		count = 0
		#Check the edge cases first. Start with 0,0 on the top left corner
		if(x == 0 and y == 0):
			if(self.getSpace(1, 0).isMine):
				count = count + 1
			if(self.getSpace(1, 1).isMine):
				count = count + 1
			if(self.getSpace(0, 1).isMine):
				count = count + 1
		#Now look at size - 1, 0 bottom left corner
		elif(x == 0 and y == self.y_size - 1): 
			if(self.getSpace(1, self.y_size - 1).isMine):
				count = count + 1
			if(self.getSpace(1, self.y_size - 2).isMine):
				count = count + 1
			if(self.getSpace(0, self.y_size - 2).isMine):
				count = count + 1
		#Look at bottom right hand corner
		elif(x == self.x_size - 1 and y == self.y_size - 1):
			if(self.getSpace(self.x_size - 2, self.y_size - 1).isMine):
				count = count + 1
			if(self.getSpace(self.x_size - 2, self.y_size - 2).isMine):
				count = count + 1
			if(self.getSpace(self.x_size - 1, self.y_size - 2).isMine):
				count = count + 1
		#Top Right Corner
		elif(x == self.x_size - 1 and y == 0):
			if(self.getSpace(self.x_size - 1, 1).isMine):
				count = count + 1
			if(self.getSpace(self.x_size - 2, 1).isMine):
				count = count + 1
			if(self.getSpace(self.x_size - 2, 0).isMine):
				count = count + 1
		#Boundary Cases Next
		#Left hand Side
		elif(x == 0):
			if(self.getSpace(0, y - 1).isMine):
				count = count + 1
			if(self.getSpace(0, y + 1).isMine):
				count = count + 1
			if(self.getSpace(1, y - 1).isMine):
				count = count + 1
			if(self.getSpace(1, y).isMine):
				count = count + 1
			if(self.getSpace(1, y + 1).isMine):
				count = count + 1
		#Right Hand Side
		elif(x == self.x_size - 1):
			if(self.getSpace(self.x_size - 1, y - 1).isMine):
				count = count + 1
			if(self.getSpace(self.x_size - 1, y + 1).isMine):
				count = count + 1
			if(self.getSpace(self.x_size - 2, y - 1).isMine):
				count = count + 1
			if(self.getSpace(self.x_size - 2, y).isMine):
				count = count + 1
			if(self.getSpace(self.x_size - 2, y + 1).isMine):
				count = count + 1
		#Top
		elif(y == 0):
			if(self.getSpace(x - 1, 0).isMine):
				count = count + 1
			if(self.getSpace(x + 1, 0).isMine):
				count = count + 1
			if(self.getSpace(x - 1, 1).isMine):
				count = count + 1
			if(self.getSpace(x, 1).isMine):
				count = count + 1
			if(self.getSpace(x + 1, 1).isMine):
				count = count + 1
		#Bottom
		elif(y == self.y_size - 1):
			if(self.getSpace(x - 1, self.y_size - 1).isMine):
				count = count + 1
			if(self.getSpace(x + 1, self.y_size - 1).isMine):
				count = count + 1
			if(self.getSpace(x - 1, self.y_size - 2).isMine):
				count = count + 1
			if(self.getSpace(x, self.y_size - 2).isMine):
				count = count + 1
			if(self.getSpace(x + 1, self.y_size - 2).isMine):
				count = count + 1
		#Finally in the middle
		else:
			if(self.getSpace(x + 1, y + 1).isMine):
				count = count + 1
			if(self.getSpace(x, y + 1).isMine):
				count = count + 1
			if(self.getSpace(x - 1, y + 1).isMine):
				count = count + 1
			if(self.getSpace(x - 1, y).isMine):
				count = count + 1
			if(self.getSpace(x + 1, y).isMine):
				count = count + 1
			if(self.getSpace(x - 1, y - 1).isMine):
				count = count + 1
			if(self.getSpace(x, y - 1).isMine):
				count = count + 1
			if(self.getSpace(x + 1, y - 1).isMine):
				count = count + 1

		self.getSpace(x, y).numOfSurroundingMines = count

	def checkFlags(self):
		isComplete = True
		for y in range(self.y_size):
			for x in range(self.x_size):
				if self.getSpace(x, y).isFlagged != self.getSpace(x,y).isBomb:
					isComplete = False
		return isComplete

	def reveal(self, x, y):
		thisSpace = self.getSpace(x, y)
		thisSpace.isRevealed = True
		if thisSpace.isMine:
			return True
		else:
			if thisSpace.numOfSurroundingMines == 0:
				x_range, y_range = range(x - 1, x + 2), range(y - 1, y + 2)
				for y_curr in y_range:
					for x_curr in x_range:
						if (x_curr >= 0 and y_curr >= 0) and (x_curr < self.x_size and y_curr < self.y_size) and not (x_curr == x and y_curr == y):
							if not self.getSpace(x_curr, y_curr).isRevealed:
								self.reveal(x_curr, y_curr)
			return False

	def toggleFlag(self, x, y):
		thisSpace = self.getSpace(x, y)
		if thisSpace.isFlagged == False:
			thisSpace.isFlagged = True
		else:
			thisSpace.isFlagged = False

	def getSpace(self, x, y):
		return self.minefield[y][x]
