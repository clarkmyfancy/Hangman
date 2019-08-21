import sys

# strict import of constructors
from Game import Game
from Player import Player

from Console import *

def main():
	game = Game()
	console = Console()

	player1 = Player("Computer 1")
	player2 = Player("Computer 2")
	players = []
	players.append(player1)
	players.append(player2)

	console.printStartupSequence()
	console.printScoreboardFor(game)

	numPlayers = len(players)
	currentPlayerId = 0
	while (game.isStillPlaying):
		currentPlayer = players[currentPlayerId]

		console.retrieveGuessFrom(currentPlayer)

		game.takeTurnFor(currentPlayer)
		console.printGuessFor(currentPlayer)
		console.printGuessedLettersFor(game)
		if not game.didPlayerJustWin(currentPlayer):
			console.printStatusFor(currentPlayer, game)
		console.printScoreboardFor(game)

		if (game.shouldEnd()):
			game.isStillPlaying = False
			console.printGameOverMessageFor(currentPlayer)

		currentPlayerId = (currentPlayerId + 1) % numPlayers
	sys.exit()

if (__name__ == '__main__'):
	main()
