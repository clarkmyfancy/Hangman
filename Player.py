import random
import string

class Player:
	guessedLetters = []
	def __init__(self, name, wrongGuessesAllowed):
		self.wrongGuessesLeft = wrongGuessesAllowed
		self.currentGuess = ''
		self.name = name

	def isOutOfGuesses(self):
		if self.wrongGuessesLeft <= 0:
			return True
		else:
			return False

	def makeGuess(self):
		newGuess = random.choice(string.ascii_lowercase)
		while(newGuess in Player.guessedLetters):
			newGuess = random.choice(string.ascii_lowercase)
		self.currentGuess = newGuess
		Player.guessedLetters.append(newGuess)
