import unittest
from Console import *

class TestConsole(unittest.TestCase):

	def setUp(self):
		self.console = Console()


	# def test_isValidInput(self):
	# 	self.assertEqual(self.console.isValidInput("3"), False)
	# 	self.assertEqual(self.console.isValidInput("74"), False)
	# 	self.assertEqual(self.console.isValidInput("fs"), False)
	# 	self.assertEqual(self.console.isValidInput("s"), True)

if (__name__ == '__main__'):
	unittest.main()
