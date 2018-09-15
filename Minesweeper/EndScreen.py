from pygame import surface, display, constants
from pygame.font import SysFont
from pygame.locals import Color

class EndScreen:
	def __init__(self, gameWon):
		self.destSurf = display.get_surface().copy()
		self.drawWindow = display.get_surface()
		self.surf = surface.Surface(display.get_surface().get_size(), constants.SRCALPHA)
		self.gameWon = gameWon
		self.winColor = (0,255, 0, 127)
		self.winTextBackgroundColor = (0,255,0)
		self.loseColor = (255, 0, 0, 127)
		self.loseTextBackgroundColor = (255,0,0)
		self.title = SysFont('lucidaconsole', 25)
		self.subtitle = SysFont('lucidaconsole', 15)

		#distance between title and subtitle text
		textMargin = 10
		#distance between edge of text and full opacity background
		textBackgroundMargin = 10

		if self.gameWon:
			self.surf.fill(self.winColor)
			self.titleSurf = self.title.render("You Won!", True, Color('black'))
		else:
			self.surf.fill(self.loseColor)
			self.titleSurf = self.title.render("You Lost...", True, Color('black'))
		self.subtitleSurf = self.subtitle.render("Click to play again", True, Color('black'))

		self.textBackgroundSurf = surface.Surface(((self.subtitleSurf.get_width() + 2*textBackgroundMargin),(self.titleSurf.get_height() + self.subtitleSurf.get_height() + textMargin + 2*textBackgroundMargin)))

		if self.gameWon:
			self.textBackgroundSurf.fill(self.winTextBackgroundColor)
		else:
			self.textBackgroundSurf.fill(self.loseTextBackgroundColor)

		self.titlePos = (self.drawWindow.get_width() / 2 - self.titleSurf.get_width() / 2, self.drawWindow.get_height() / 2 - self.titleSurf.get_height() - textMargin / 2)
		self.subtitlePos = (self.drawWindow.get_width() / 2 - self.subtitleSurf.get_width() / 2, self.drawWindow.get_height() / 2 + textMargin / 2)
		self.textBackgroundPos = (self.drawWindow.get_width() / 2 - self.textBackgroundSurf.get_width() / 2, self.drawWindow.get_height() / 2 - self.textBackgroundSurf.get_height() / 2)

	def render(self):
		self.drawWindow.blit(self.destSurf, (0,0))
		self.drawWindow.blit(self.surf, (0,0), None, constants.BLEND_RGBA_MULT)
		self.drawWindow.blits([
			(self.textBackgroundSurf, self.textBackgroundPos),
			(self.titleSurf, self.titlePos),
			(self.subtitleSurf, self.subtitlePos)
		])

		display.flip()	