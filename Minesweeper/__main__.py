import pygame
from pygame.locals import *
from Minesweeper.Minesweeper import Minesweeper
from Minesweeper.Minefield import Minefield
from Minesweeper.Graphics.Window import Window
from Minesweeper.Graphics.StartScreen import StartScreen
from Minesweeper.Graphics.EndScreen import EndScreen
from Minesweeper.Graphics.Drawer import Drawer

def main():	
	states = {
		'Start': 1,
		'App': 2, 
		'End': 3, 
	}
	currentState = states['Start']
	startScreen = None
	minesweeper = None
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
		
		minesweeper = Minesweeper(startScreen.x_size, startScreen.y_size, startScreen.numMines)
		gameRunning = True
		while gameRunning:
			for event in pygame.event.get():
				# Quit Event 
				if event.type == pygame.QUIT:
					pygame.quit()
					return 0
				elif event.type == pygame.MOUSEBUTTONDOWN:
					(end, win) = minesweeper.onClick(event)
					if end:
						if win == 'RESET':
							pass
						else:
							if not win:
								minesweeper.onLose()
							endScreen = EndScreen(win)
						gameRunning = False
						#app.window.gameScreen.unlock()
				minesweeper.updateFlags()
			minesweeper.render()
			minesweeper.window.clock.tick(60)
		if minesweeper.reset_flag:
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
			minesweeper.window.clock.tick(60)

main()