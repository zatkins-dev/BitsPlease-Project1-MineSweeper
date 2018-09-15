from pygame import mouse, font, surface, constants

class Drawer:
    def __init__(self):
        self.buttonIsClicked = False
        
    def drawButton(self, destSurf, x, y, width, height, color, colorHover, buttonText, buttonTextSize, buttonFunction=None):
        mousePos = mouse.get_pos()
        t_font = font.SysFont('lucidaconsole', buttonTextSize)
        text = t_font.render(str(buttonText), True, (0,0,0))

        button = surface.Surface((width, height), constants.SRCALPHA)

        offset = destSurf.get_abs_offset()

        #see if mouse is within the area of our button
        if mousePos[0] > x + offset[0] and mousePos[0] < x + width + offset[0] and mousePos[1] > y + offset[1] and mousePos[1] < y + height + offset[1]:
            #mouse is over the button
            button.fill(colorHover)
			#mouse is in the button, so it may click the button and run its function
            if mouse.get_pressed()[0] and buttonFunction != None and not self.buttonIsClicked:
                buttonFunction()
                self.buttonIsClicked = True
            elif not mouse.get_pressed()[0] and self.buttonIsClicked:
                self.buttonIsClicked = False
        else:
			#mouse isn't in the button
            button.fill(color)

		#put button onto the screen, then text onto the screen centered over the button
        destSurf.blits([
            (button, (x, y)),
            (text, (x + width / 2 - text.get_width() / 2, y + height / 2 - text.get_height() / 2))
        ])