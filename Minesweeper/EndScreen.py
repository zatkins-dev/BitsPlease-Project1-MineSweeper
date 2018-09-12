import pygame
from Minesweeper.StartScreen import StartScreen

class EndScreen:
    def __init__(self, gameWon, windowSize):
        self.surf = pygame.Surface(windowSize, pygame.SRCALPHA)
        self.destSurf = pygame.display.get_surface().copy()
        self.drawWindow = pygame.display.get_surface()
        self.gameWon = gameWon
        self.winColor = (0,255, 0, 127)
        self.loseColor = (255, 0, 0, 127)

        if self.gameWon:
            self.surf.fill(self.winColor)
        else:
            self.surf.fill(self.loseColor)
            
    def render(self):
        self.drawWindow.blits([
            (self.destSurf, (0,0)),
            (self.surf, (0,0))
        ])
        pygame.display.flip()

        