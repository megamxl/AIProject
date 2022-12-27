import unittest

from Puzzle import Puzzle
from solvers import AStar, Manhattan, Hamming, BranchAndBound


class AStarTests(unittest.TestCase):

    def test_find_zero(self):
        new_puzzle = Puzzle([[7, 3, 4], [5, 6, 0], [2, 8, 1]])
        zero_position = AStar.find0(new_puzzle.grid)

        self.assertEqual((1, 2), zero_position)

    def test_possible_moves(self):
        moves = AStar.possibleMoves((1, 2), 'D')
        expected_moves = [(0, -1), (1, 0)]

        self.assertEqual(expected_moves, moves)

    def test_move_tile(self):
        new_puzzle = Puzzle([[7, 3, 4], [5, 6, 0], [2, 8, 1]])

        self.assertEqual([[7, 3, 4], [5, 0, 6], [2, 8, 1]], AStar.moveTile(new_puzzle.grid, (0, -1)))
        self.assertEqual([[7, 3, 4], [0, 5, 6], [2, 8, 1]], AStar.moveTile(new_puzzle.grid, (0, -1)))
        self.assertEqual([[7, 3, 4], [2, 5, 6], [0, 8, 1]], AStar.moveTile(new_puzzle.grid, (1, 0)))

    def test_search_hamming(self):
        testPuzzle = Puzzle()
        result = AStar.aStar(testPuzzle, Hamming)
        self.assertEqual(Puzzle([[0, 1, 2], [3, 4, 5], [6, 7, 8]]), result)

    def test_search_manhattan(self):
        testPuzzle = Puzzle()
        result = AStar.aStar(testPuzzle, Manhattan)
        self.assertEqual(Puzzle([[0, 1, 2], [3, 4, 5], [6, 7, 8]]), result)

    def test_search_bab(self):
        testPuzzle = Puzzle()
        result = AStar.aStar(testPuzzle, BranchAndBound)
        self.assertEqual(Puzzle([[0, 1, 2], [3, 4, 5], [6, 7, 8]]), result)


if __name__ == '__main__':
    unittest.main()
