import pygame

class EndScreen:
	def __init__(self, gameWon):
		self.destSurf = pygame.display.get_surface().copy()
		self.drawWindow = pygame.display.get_surface()
		self.surf = pygame.Surface(pygame.display.get_surface().get_size(), pygame.SRCALPHA)
		self.gameWon = gameWon
		self.winColor = (0,255, 0, 127)
		self.winTextBackgroundColor = (0,255,0)
		self.loseColor = (255, 0, 0, 127)
		self.loseTextBackgroundColor = (255,0,0)
		self.title = pygame.font.SysFont('lucidaconsole', 25)
		self.subtitle = pygame.font.SysFont('lucidaconsole', 15)

		#distance between title and subtitle text
		textMargin = 10
		#distance between edge of text and full opacity background
		textBackgroundMargin = 10

		if self.gameWon:
			self.surf.fill(self.winColor)
			self.titleSurf = self.title.render("You Won!", True, pygame.Color('black'))
		else:
			self.surf.fill(self.loseColor)
			self.titleSurf = self.title.render("You Lost...", True, pygame.Color('black'))
		self.subtitleSurf = self.subtitle.render("Click to play again", True, pygame.Color('black'))

		self.textBackgroundSurf = pygame.Surface(((self.subtitleSurf.get_width() + 2*textBackgroundMargin),(self.titleSurf.get_height() + self.subtitleSurf.get_height() + textMargin + 2*textBackgroundMargin)))

		if self.gameWon:
			self.textBackgroundSurf.fill(self.winTextBackgroundColor)
		else:
			self.textBackgroundSurf.fill(self.loseTextBackgroundColor)

		self.titlePos = (self.drawWindow.get_width() / 2 - self.titleSurf.get_width() / 2, self.drawWindow.get_height() / 2 - self.titleSurf.get_height() - textMargin / 2)
		self.subtitlePos = (self.drawWindow.get_width() / 2 - self.subtitleSurf.get_width() / 2, self.drawWindow.get_height() / 2 + textMargin / 2)
		self.textBackgroundPos = (self.drawWindow.get_width() / 2 - self.textBackgroundSurf.get_width() / 2, self.drawWindow.get_height() / 2 - self.textBackgroundSurf.get_height() / 2)

	def render(self):
		self.drawWindow.blit(self.destSurf, (0,0))
		self.drawWindow.blit(self.surf, (0,0), None, pygame.BLEND_RGBA_MULT)
		self.drawWindow.blits([
			(self.textBackgroundSurf, self.textBackgroundPos),
			(self.titleSurf, self.titlePos),
			(self.subtitleSurf, self.subtitlePos)
		])

		pygame.display.flip()	