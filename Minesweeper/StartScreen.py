import pygame
from pygame.locals import *

class StartScreen:
    def __init__(self):
        pygame.init()
        self.x_size = 9
        self.y_size = 9
        self.numMines = 10
        self.window_x_size = 600
        self.window_y_size = 400
        self.window_margin = 20
        self.window = pygame.display.set_mode((self.window_x_size, self.window_y_size))
        self.sizeSurface = self.window.subsurface(Rect(self.window_margin, self.window_margin, self.window_x_size / 2 - 1.5*self.window_margin, self.window_y_size - 2*self.window_margin))
        self.minesSurface = self.window.subsurface(Rect((self.window_x_size / 2) + .5*self.window_margin, self.window_margin, self.window_x_size / 2 - 1.5*self.window_margin, self.window_y_size - 2*self.window_margin))
        self.window.fill(Color('light grey'))
        self.sizeSurface.fill(Color('dark grey'))
        self.minesSurface.fill(Color('dark gray'))
        self.clock = pygame.time.Clock()

    def render(self):
        sizeLabelSurf = self.drawText("Size:", self.sizeSurface, (0, 20), 30, Color('black'))
        self.drawText("Width:", self.sizeSurface, (40, 80), 25, Color('black'))
        self.drawText("Height:", self.sizeSurface, (140, 80), 25, Color('black'))
        

        pygame.display.flip()

    def drawButton(self, destSurf, x, y, width, height, color, colorHover, buttonText, buttonTextSize, buttonFunction=None):
        mousePos = pygame.mouse.get_pos()
        font = pygame.font.SysFont('lucidaconsole', buttonTextSize)
        text = font.render(str(buttonText), True, (0,0,0))

        button = pygame.Surface((width, height), pygame.SRCALPHA)

        #see if mouse is within the area of our button
        if mousePos[0] > x and mousePos[0] < x + width and mousePos[1] > y and mousePos[1] < y + height:
            #mouse is over the button
            button.fill(colorHover)

			#mouse is in the button, so it may click the button and run its function
            if pygame.mouse.get_pressed()[0] and buttonFunction != None:
                buttonFunction()
        else:
			#mouse isn't in the button
            button.fill(color)

		#put button onto the screen, then text onto the screen centered over the button
        destSurf.blits([
            (button, (x, y)),
            (text, (x + width / 2 - text.get_width() / 2, y + height / 2 - text.get_height() / 2))
        ])

    def drawText(self, text, destSurf, position, size, color):
        font = pygame.font.SysFont('lucidaconsole', size)
        textSurf = font.render(str(text), True, color)
        destSurf.blit(textSurf, position)
        return textSurf
