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
		setMines()

		#initialize surrounding mine numbers
		for y in range(self.y_size):
			for x in range(self.x_size):
				checkNeighbors(x, y)

	def setMines(self):

		currentMines = 0
		random.seed()

		while currentMines <= numMines:
			mine_x, mine_y = randrange(self.x_size), randrange(self.y)
			thisSpace = self.getSpace(mine_x, mine_y)

			if not thisSpace.is_Mine:
				thisSpace.isMine = True
				currentMines += 1

    def checkNeighbors(self, x, y):
		pass
	def checkFlags(self):
        isComplete = True
        for y in range(self.y_size):
            for x in range(self.x_size):
                if getSpace(x, y).isFlagged != getSpace(x,y).isBomb:
                    isComplete = False
        return isComplete

    def reveal(self, x, y):
		pass


    def toggleFlag(self, x, y):
        thisSpace = getSpace(x, y)
        if thisSpace.isFlagged == False:
            thisSpace.isFlagged = True
        else:
            thisSpace.isFlagged = False

    def getSpace(self, x, y):
        return minefield[y][x]
