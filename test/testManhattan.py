import unittest

from Puzzle import Puzzle
from solvers import Manhattan

SOLVE_STATE = Puzzle([[0, 1, 2], [3, 4, 5], [6, 7, 8]])


class ManhattanTests(unittest.TestCase):
    def test_distanceCalc(self):
        distance0 = Manhattan.calc([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
        distance20 = Manhattan.calc([[8, 7, 6], [5, 4, 3], [2, 1, 0]])
        distance19 = Manhattan.calc([[7, 3, 4], [5, 6, 0], [2, 8, 1]])

        self.assertEqual(0, distance0)
        self.assertEqual(20, distance20)
        self.assertEqual(19, distance19)


if __name__ == '__main__':
    unittest.main()
