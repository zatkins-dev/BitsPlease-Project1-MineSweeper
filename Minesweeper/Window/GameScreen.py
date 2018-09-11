from pygame import Surface

class GameScreen(Surface):
    def __init__(self, x_dim, y_dim):
        Surface.__init__(self, (x_dim*32, y_dim*32))