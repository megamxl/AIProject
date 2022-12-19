import unittest
from Puzzle import *


class PuzzleTests(unittest.TestCase):

    def test_isSolvable(self):
        testP = Puzzle([[1, 8, 2], [0, 4, 3], [7, 6, 5]])
        self.assertEqual(True, testP.isSolvable())

    def test_isNotSolvable(self):
        testP = Puzzle([[8, 1, 2], [0, 4, 3], [7, 6, 5]])
        self.assertEqual(False, testP.isSolvable())


if __name__ == '__main__':
    unittest.main()
