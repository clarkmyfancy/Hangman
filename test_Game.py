import unittest
from Game import getRandomWord

class TestGame(unittest.TestCase):

	def setUp(self):
		self.game = Game()

	def tearDown(self):
		pass

	def test_getRandomWord(self):
		self.assertIsNotNone(self.game.getRandomWord())


if __name__ == '__main__':
	unittest.main()
