from pygame import event, constants
from enum import Enum
from Minesweeper.Minesweeper import Minesweeper
from Minesweeper.Minefield import Minefield
from Minesweeper.StartScreen import StartScreen
from Minesweeper.EndScreen import EndScreen

def main():
	"""
	The __main__ class utilizes a finite state machine structure to manage the overall flow
	of the game from start up to game ending.

	**States**
		There are four states that the game undergoes. The states and their interactions summarized:

		*Start*: The default state when the game is first run. This state creates the StartScreen, which
		asks players what board size they perfer and the number of mines on the board. This state will end
		either when the player quits the game with a state *Exit* or generates a game with a state *Minesweeper*.

		*Minesweeper*: This state runs when the player is actually playing minesweeper. There are only two ways to

		*End*:

		*Exit*:

	**Args**:
			None.

	**Preconditions**:
			None.

	**Postconditions**:
			None.

	**Returns**:
			None.
	"""
	State = Enum('State','Start Minesweeper End Exit')
	currentState = State.Start
	startScreen = None
	minesweeper = None
	endScreen = None
	while currentState != State.Exit:
		if (currentState == State.Start):
			if startScreen is None:
				startScreen = StartScreen()
			for newEvent in event.get():
				if newEvent.type == constants.QUIT:
					currentState = State.Exit
			startScreen.render()
			startScreen.clock.tick(60)
			if startScreen.gameReady:
				currentState = State.Minesweeper
				minesweeper = Minesweeper(startScreen.x_size, startScreen.y_size, startScreen.numMines)
				startScreen = None

		elif currentState == State.Minesweeper:
			for newEvent in event.get():
				if newEvent.type == constants.QUIT:
					currentState = State.Exit
				elif newEvent.type == constants.MOUSEBUTTONDOWN:
					(end, win) = minesweeper.onClick(newEvent)
					if end:
						if win is None:
							currentState = State.Start
						else:
							currentState = State.End
							if not win:
								minesweeper.onLose()
							minesweeper.render()
							endScreen = EndScreen(win)
			minesweeper.render()
			minesweeper.window.clock.tick(60)

		elif currentState == State.End:
			endScreen.render()
			minesweeper.window.clock.tick(60)

			for newEvent in event.get():
				if newEvent.type == constants.QUIT:
					currentState = State.Exit
				elif newEvent.type == constants.MOUSEBUTTONDOWN:
					currentState = State.Start
					endScreen = None
		else:
			currentState = State.Start
			print('Error: This really should never happen, resetting game...')


main()
