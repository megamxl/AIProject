import unittest

from DataClasses.Puzzle import *


class PuzzleTests(unittest.TestCase):

    def test_static_init(self):
        new_puzzle = Puzzle()
        new_puzzle.setGrid([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
        self.assertEqual([[0, 1, 2], [3, 4, 5], [6, 7, 8]], new_puzzle.grid)

    def test_dynamic_init(self):
        new_puzzle = Puzzle()
        gridList = sum(new_puzzle.grid, [])

        self.assertEqual(3, len(new_puzzle.grid))
        self.assertEqual(3, len(new_puzzle.grid[0]))
        self.assertEqual(3, len(new_puzzle.grid[1]))
        self.assertEqual(3, len(new_puzzle.grid[2]))

        for x in range(9):
            self.assertTrue(x in gridList)

    def test_set_grid(self):
        new_puzzle = Puzzle()
        new_puzzle.setGrid([[1, 8, 2], [0, 4, 3], [7, 6, 5]])
        self.assertEqual([[1, 8, 2], [0, 4, 3], [7, 6, 5]], new_puzzle.grid)

    def test_is_solvable(self):
        testP = Puzzle()
        testP.setGrid([[1, 8, 2], [0, 4, 3], [7, 6, 5]])
        self.assertEqual(True, testP.isSolvable())

    def test_is_not_solvable(self):
        testP = Puzzle()
        testP.setGrid([[8, 1, 2], [0, 4, 3], [7, 6, 5]])
        self.assertEqual(False, testP.isSolvable())


if __name__ == '__main__':
    unittest.main()
