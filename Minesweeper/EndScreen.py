from pygame import surface, display, constants
from pygame.font import SysFont
from pygame.locals import Color

class EndScreen:
	def __init__(self, gameWon):
		self.destSurf = display.get_surface().copy()
		self.drawWindow = display.get_surface()
		self.surf = surface.Surface(display.get_surface().get_size(), constants.SRCALPHA)

		color = (0,255, 0, 127) if gameWon else (255, 0, 0, 127)
		text = "You Won!" if gameWon else "You Lost..."
		backgroundColor = (0,255,0) if gameWon else (255,0,0)
		title = SysFont('lucidaconsole', 25)
		subtitle = SysFont('lucidaconsole', 15)

		#distance between title and subtitle text
		textMargin = 10
		#distance between edge of text and full opacity background
		textBackgroundMargin = 10

		self.surf.fill(color)
		self.titleSurf = title.render(text, True, Color('black'))
		self.subtitleSurf = subtitle.render("Click to play again", True, Color('black'))

		self.textBackgroundSurf = surface.Surface(
			(self.subtitleSurf.get_width() + 2*textBackgroundMargin),
			(self.titleSurf.get_height() + self.subtitleSurf.get_height() + textMargin + 2*textBackgroundMargin)
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
		self.drawWindow.blit(self.destSurf, (0,0))
		self.drawWindow.blit(self.surf, (0,0), None, constants.BLEND_RGBA_MULT)
		self.drawWindow.blits([
			(self.textBackgroundSurf, self.textBackgroundPos),
			(self.titleSurf, self.titlePos),
			(self.subtitleSurf, self.subtitlePos)
		])

		display.flip()	