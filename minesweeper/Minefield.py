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
        count = 0;
        #Check the edge cases first. Start with 0,0 on the top left corner
        if(x == 0 and y == 0):
            if(getSpace(self, 1, 0).is_Mine):
                count = count + 1
            if(getSpace(self, 1, 1).is_Mine):
                count = count + 1
            if(getSpace(self, 0, 1).is_Mine):
                count = count + 1
        #Now look at size - 1, 0 bottom left corner
        elif(x == 0 and y == self.ysize - 1): 
            if(getSpace(self, 1, self.ysize - 1).is_Mine):
                count = count + 1
            if(getSpace(self, 1, self.ysize - 2).is_Mine):
                count = count + 1
            if(getSpace(self, 0, self.ysize - 2).is_Mine):
                count = count + 1
        #Look at bottom right hand corner
        elif(x == self.xsize - 1 and y == self.ysize - 1):
            if(getSpace(self, self.xsize - 2, self.ysize - 1).is_Mine:
                count = count + 1
            if(getSpace(self, self.xsize - 2, self.ysize - 2).is_Mine):
                count = count + 1
            if(getSpace(self, self.xsize - 1, self.ysize - 2).is_Mine):
                count = count + 1
        #Top Right Corner
        elif(x == self.size - 1 and y == 0):
            if(getSpace(self, self.xsize - 1, 1).is_Mine):
                count = count + 1
            if(getSpace(self, self.xsize - 2, 1).is_Mine):
                count = count + 1
            if(getSpace(self, self.xsize - 2, 0).is_Mine):
                count = count + 1
        #Boundary Cases Next
        #Left hand Side
        elif(x == 0):
            if(getSpace(self, 0, y - 1).is_Mine):
                count = count + 1
            if(getSpace(self, 0, y + 1).is_Mine):
                count = count + 1
            if(getSpace(self, 1, y - 1).is_Mine):
                count = count + 1
            if(getSpace(self, 1, y).is_Mine):
                count = count + 1
            if(getSpace(self, 1, y + 1).is_Mine):
                count = count + 1
        #Right Hand Side
        elif(x == self.xsize - 1):
            if(getSpace(self, self.xsize - 1, y - 1).is_Mine):
                count = count + 1
            if(getSpace(self, self.xsize - 1, y + 1).is_Mine):
                count = count + 1
            if(getSpace(self, self.xsize - 2, y - 1).is_Mine):
                count = count + 1
            if(getSpace(self, self.xsize - 2, y).is_Mine):
                count = count + 1
            if(getSpace(self, self.xsize - 2, y + 1).is_Mine):
                count = count + 1
        #Top
        elif(y == 0):
            if(getSpace(self, x - 1, 0).is_Mine):
                count = count + 1
            if(getSpace(self, x + 1, 0).is_Mine):
                count = count + 1
            if(getSpace(self, x - 1, 1).is_Mine):
                count = count + 1
            if(getSpace(self, x, 1).is_Mine):
                count = count + 1
            if(getSpace(self, x + 1, 1).is_Mine):
                count = count + 1
        #Bottom
        elif(y == self.ysize - 1):
            if(getSpace(self, x - 1, self.ysize - 1).is_Mine):
                count = count + 1
            if(getSpace(self, x + 1, self.ysize - 1).is_Mine):
                count = count + 1
            if(getSpace(self, x - 1, self.ysize - 2).is_Mine):
                count = count + 1
            if(getSpace(self, x, self.ysize - 2).is_Mine):
                count = count + 1
            if(getSpace(self, x + 1, self.ysize - 2).is_Mine):
                count = count + 1
        #Finally in the middle
        else:
            if(getSpace(self, x + 1, y + 1).is_Mine):
                count = count + 1
            if(getSpace(self, x, y + 1).is_Mine):
                count = count + 1
            if(getSpace(self, x - 1, y + 1).is_Mine):
                count = count + 1
            if(getSpace(self, x - 1, y).is_Mine):
                count = count + 1
            if(getSpace(self, x + 1, y).is_Mine):
                count = count + 1
            if(getSpace(self, x - 1, y - 1).is_Mine):
                count = count + 1
            if(getSpace(self, x - 1, y).is_Mine):
                count = count + 1
            if(getSpace(self, x - 1, y + 1).is_Mine)::
                count = count + 1

        getSpace(self, x, y).numOfSurroundingMines = count

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
