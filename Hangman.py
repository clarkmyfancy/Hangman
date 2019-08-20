import sys

from Game import Game
from Player import Player
from Console import *

# two random letter generators battle it out!
# Computer 1 vs. Computer 2 battling it out in the oldest game in the books.
# who will wither away, who will reign supreme? who can stand this cliché??

def main():
	game = Game()
	console = Console()

	wrongGuessesAllowed = game.wrongGuessesPerPlayer
	player1 = Player("Computer 1", wrongGuessesAllowed)
	player2 = Player("Computer 2", wrongGuessesAllowed)
	players = []
	players.append(player1)
	players.append(player2)

	console.printStartupSequence()
	console.printScoreboardForGame(game)

	numPlayers = len(players)
	currentPlayerId = 0
	while (game.gameInPlay):
		currentPlayer = players[currentPlayerId]

		console.retrieveGuessFromPlayer(currentPlayer)

		game.takeTurnForPlayer(currentPlayer)
		console.printGuessForPlayer(currentPlayer)
		console.printGuessedLettersForGame(game)
		if not game.didPlayerJustWin(currentPlayer):
			console.printStatusForPlayer(currentPlayer)
		console.printScoreboardForGame(game)

		if (game.shouldEndForPlayer(currentPlayer)):
			game.gameInPlay = False
			console.printGameOverMessageForPlayer(currentPlayer)
		currentPlayerId = (currentPlayerId + 1) % numPlayers
	sys.exit()

if (__name__ == '__main__'):
	main()
