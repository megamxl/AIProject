import unittest

from Puzzle import Puzzle
from solvers import Hamming


class HammingTests(unittest.TestCase):
    def test_solve_static(self):
        testPuzzle = Puzzle()
        result = Hamming.solve(testPuzzle)
        self.assertEqual(Puzzle([[0, 1, 2], [3, 4, 5], [6, 7, 8]]), result)

    def test_solve_dynamic(self):
        testPuzzleA = Puzzle()
        testPuzzleB = Puzzle()
        resultA = Hamming.solve(testPuzzleA)
        resultB = Hamming.solve(testPuzzleB)
        self.assertEqual(resultA, resultB)


if __name__ == '__main__':
    unittest.main()
