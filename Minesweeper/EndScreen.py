import pygame
from StartScreen import drawButton

class EndScreen:
    def __init__(self, gameWon, windowSize):
        self.surf = pygame.Surface(windowSize, pygame.SRCALPHA)
        self.gameWon = gameWon
        self.winColor = (0,255, 0, 127)
        self.loseColor = (255, 0, 0, 127)

    def render(self):
        if self.gameWon:
            self.surf.fill(self.winColor)
        else:
            self.surf.fill(self.loseColor)