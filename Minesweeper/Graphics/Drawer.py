from pygame import mouse, font, surface, constants

class Drawer:
    def __init__(self):
        self.buttonIsClicked = False
        
    def drawButton(self, destSurf, pos, size, colors, buttonText, buttonTextSize, buttonFunction=None):
        mousePos = mouse.get_pos()
        t_font = font.SysFont('lucidaconsole', buttonTextSize)
        text = t_font.render(str(buttonText), True, (0,0,0))

        button = surface.Surface(size, constants.SRCALPHA)

        offset = destSurf.get_abs_offset()

        #see if mouse is within the area of our button
        if mousePos[0] > pos[0] + offset[0] and mousePos[0] < pos[0] + size[0] + offset[0] and mousePos[1] > pos[1] + offset[1] and mousePos[1] < pos[1] + size[1] + offset[1]:
            #mouse is over the button
            button.fill(colors[1])
			#mouse is in the button, so it may click the button and run its function
            if mouse.get_pressed()[0] and buttonFunction != None and not self.buttonIsClicked:
                buttonFunction()
                self.buttonIsClicked = True
            elif not mouse.get_pressed()[0] and self.buttonIsClicked:
                self.buttonIsClicked = False
        else:
			#mouse isn't in the button
            button.fill(colors[0])

		#put button onto the screen, then text onto the screen centered over the button
        destSurf.blits([
            (button, pos),
            (text, (pos[0] + size[0] / 2 - text.get_width() / 2, pos[1] + size[1] / 2 - text.get_height() / 2))
        ])