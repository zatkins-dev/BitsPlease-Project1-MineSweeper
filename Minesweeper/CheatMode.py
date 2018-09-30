from pygame import surface, display, constants
from pygame.font import SysFont
from pygame.locals import Color

class CheatMode:
	"""CheatMode adds a blue screen on top while cheat mode is executed

	**Class Variables**:
		*gameSurf*: Surface A copy of the game screen to be used as a base for other transparent drawing

		*drawWindow*: Surface The active game surface to draw to

		*transparentSurf*: Surface A transparent surface to draw. Will be green on a win, and red on a loss.

		*titleSurf*: Surface A rendering of more emphasized text, such as "You Won!"

		*subtitleSurf*: Surface A rendering of less emphasized text, such as "Click to play again..."

		*textBackgroundSurf*: Surface A background to put behind the rendered text

		*titlePos*: Tuple (Int, Int) Holds the (x,y) corrdinates of the title surface

		*subtitlePos*: Tuple (Int, Int) Holds the (x,y) coordinates of the subtitle surface

		*textBackgroundPos*: Tuple (Int, Int) Holds the (x,y) coordinates of the text's background
	"""

	def __init__(self):
		self.drawWindow = display.get_surface()

		backgroundColor = (31, 97, 141, 200)
		title = SysFont('lucidaconsole', 25)
		subtitle = SysFont('lucidaconsole', 15)

        #distance between title and subtitle text
		textMargin = 10
        #distance between edge of text and full opacity background
		textBackgroundMargin = 10

		self.titleSurf = title.render("Cheat mode", True, Color('black'))
		self.subtitleSurf = subtitle.render("Click to exit", True, Color('black'))

		self.textBackgroundSurf = surface.Surface(
			(self.subtitleSurf.get_width() + 2*textBackgroundMargin + 50,
			self.titleSurf.get_height() + self.subtitleSurf.get_height() + textMargin + 2*textBackgroundMargin)
		)


		self.textBackgroundSurf.fill(backgroundColor)

		self.titlePos = (
			self.drawWindow.get_width() / 2 - self.titleSurf.get_width() / 2,
			self.drawWindow.get_height() / 2 - self.titleSurf.get_height() - textMargin / 2
		)
		self.subtitlePos = (
			self.drawWindow.get_width() / 2 - self.subtitleSurf.get_width() / 2,
			self.drawWindow.get_height() / 2 + textMargin / 2
		)
		self.textBackgroundPos = (
			self.drawWindow.get_width() / 2 - self.textBackgroundSurf.get_width() / 2,
			self.drawWindow.get_height() / 2 - self.textBackgroundSurf.get_height() / 2
		)



	def render(self):
		self.drawWindow.blits([
    		(self.textBackgroundSurf, self.textBackgroundPos),
			(self.titleSurf, self.titlePos),
    		(self.subtitleSurf, self.subtitlePos)
    	])
		display.flip()
