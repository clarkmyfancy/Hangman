class Console:

	def printStartupSequence(self):
		print("Let's play Hangman!")

	def printScoreboardForGame(self, game):
		word = game.secretWord
		isLetterRevealed = game.lettersRevealed
		outputString = ""
		for x in range(0, len(word)):
			outputString += word[x] if isLetterRevealed[x] == True else "_"
			outputString += ' '
		print(outputString)
		print("\n")

	def printGuessedLettersForGame(self, game):
		for i, x in enumerate(game.guessedLetters):
			if i == len(game.guessedLetters) - 1:
				print(x)
				print()
			else:
				print(x + " ", end="")

	def retrieveGuessFromPlayer(self, player):
		print(player.name + ", enter guess: ")

	def printGuessForPlayer(self, player):
		print(str(player.name) + " guessed: " + player.currentGuess)

	def printStatusForPlayer(self, player):
		context = "Incorrect guesses left for "
		print(context + player.name + ": " + str(player.wrongGuessesLeft))

	def printGameOverMessageForPlayer(self, player):
		print("And that's it, \'" + player.name + "\' is out of guesses.")
		print(player.name + ", Game Over")
