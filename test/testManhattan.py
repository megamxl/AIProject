import unittest

from Puzzle import Puzzle
from solvers import Manhattan


class ManhattanTests(unittest.TestCase):
    def test_solve_static(self):
        testPuzzle = Puzzle()
        result = Manhattan.solve(testPuzzle)
        self.assertEqual(Puzzle([[0, 1, 2], [3, 4, 5], [6, 7, 8]]), result)

    def test_solve_dynamic(self):
        testPuzzleA = Puzzle()
        testPuzzleB = Puzzle()
        resultA = Manhattan.solve(testPuzzleA)
        resultB = Manhattan.solve(testPuzzleB)
        self.assertEqual(resultA, resultB)

if __name__ == '__main__':
    unittest.main()
