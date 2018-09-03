class Space:
    def __init__(self, x_loc, y_loc, is_Mine):
        self.x_loc = x_loc
        self.y_loc = y_loc
        self.is_Mine = is_Mine
        self.isFlagged = False
        self.isRevealed = False
        self.numOfSurroundingMines = 0



    
