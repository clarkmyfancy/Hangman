# from random_word import RandomWords

class Game:

	def __init__(self):
		try:
			# r = RandomWords()
			# self.secretWord = r.get_random_word(maxLength = 8)
		# except:
			print("Could not connect to RandomWords library.")
			print()
			self.secretWord = input("Enter your mystery word: ")
			# self.secretWord =
		finally:
			self.lettersRevealed = [False] * len(self.secretWord)
			self.revealHyphensAndSpaces()
			self.gameInPlay = True
			self.wrongGuessesPerPlayer = 15
			self.guessedLetters = []
			self.wrongGuessesLeft = 6

	def revealHyphensAndSpaces(self):
		i = 0
		if ('-' in self.secretWord):
			i = self.secretWord.find('-')
			self.lettersRevealed[i] = True
		if (' ' in self.secretWord):
			i = self.secretWord.find('-')
			self.lettersRevealed[i] = True

	def takeTurnFor(self, player):
		player.makeGuess()
		self.checkGuessOf(player)


	def checkGuessOf(self, player):
		guess = player.currentGuess
		self.guessedLetters.append(guess)
		isLetterInWord = False
		word = self.secretWord
		for x in range(0, len(word)):
			if self.lettersRevealed[x] == False:
				if guess == word[x]:
					self.lettersRevealed[x] = True
					isLetterInWord = True
		if not isLetterInWord:
			player.wrongGuessesLeft -= 1

	def didPlayerJustWin(self, player):
		return False if (False in self.lettersRevealed) else True
	 

	def shouldEndFor(self, player):
		if self.isPuzzleComplete():
			return True
		if player.isOutOfGuesses():
			return True

	def isPuzzleComplete(self):
		correctGuesses = 0
		for x in self.lettersRevealed:
			if x == True:
				correctGuesses += 1
		if correctGuesses == len(self.secretWord):
			return True
		else:
			return False

	def isOutOfGuesses(self):
		if self.wrongGuessesLeft <= 0:
			return True
		else:
			return False
