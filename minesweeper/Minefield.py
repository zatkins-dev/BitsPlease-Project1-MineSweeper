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
		for y in range(self.y_size):
			self.minefield[y] = []
			for x in range(self.x_size):
				self.minefield[y][x] = Space(x, y)

		#set mines in the minefield

		#initialize surrounding mine numbers

	def setMines(self):

		currentMines = 0
		random.seed()

		while currentMines <= numMines:
			mine_x, mine_y = randrange(self.x_size), randrange(self.y)


    def checkNeighbors(self, x, y):
		pass
	def checkFlags(self):

		pass
    def placeFlag(self, x, y):
        getSpace(x, y).isFlagged = True

    def reveal(self, x, y):
		pass
    def removeFlag(self, x, y):
        getSpace(x, y).isFlagged = False

    def getSpace(self, x, y):
        return minefield[y][x]
