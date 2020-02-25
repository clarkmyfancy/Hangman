import unittest
from Player import *

class TestPlayer(unittest.TestCase):

	def setUp(self):
		self.player = Player()

	def tearDown(self):
		del self.player

	def test_makeNewGuess(self):
		pass
		# self.assertIsNotNone(self.player.makeNewGuess())

		# WOAH this above is an interesting test case, how to do it?


if __name__ == '__main__':
	unittest.main()