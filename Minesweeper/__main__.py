import pygame
from pygame.locals import *
from Minesweeper.Minefield import Minefield
from Minesweeper.Graphics.Window import Window
from Minesweeper.Graphics.StartScreen import StartScreen
from Minesweeper.Graphics.EndScreen import EndScreen
from Minesweeper.Graphics.Drawer import Drawer

def main():	
	startScreen = None
	app = None
	endScreen = None
	while True:
	
		startScreen = StartScreen()
		gameStarting = True
		while gameStarting:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					return 0
			startScreen.render()
			gameStarting = not startScreen.gameReady
			startScreen.clock.tick(60)
		
		app = App(startScreen.x_size, startScreen.y_size, startScreen.numMines)
		gameRunning = True
		while gameRunning:
			for event in pygame.event.get():
				# Quit Event 
				if event.type == pygame.QUIT:
					pygame.quit()
					return 0
				elif event.type == pygame.MOUSEBUTTONDOWN:
					(end, win) = app.onClick(event)
					if end:
						#app.window.gameScreen.lock()
						# TODO: Game over screen
						if win == 'RESET':
							pass
						else:
							if not win:
								app.onLose()
							endScreen = EndScreen(win)
						gameRunning = False
						#app.window.gameScreen.unlock()
				app.updateFlags()
			app.render()
			app.window.clock.tick(60)
		if app.reset_flag:
			continue
		gameEnding = True
		while gameEnding:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					return 0
				elif event.type == pygame.MOUSEBUTTONDOWN:
					gameEnding = False
			
			endScreen.render()
			app.window.clock.tick(60)