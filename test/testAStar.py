import unittest

from DataClasses.Node import Node
from DataClasses.Puzzle import Puzzle
from Solvers import AStar
from Heuristics import Hamming, Manhattan


class AStarTests(unittest.TestCase):

    def test_find_zero(self):
        new_puzzle = Puzzle()
        new_puzzle.grid = [[7, 3, 4], [5, 6, 0], [2, 8, 1]]
        zero_position = AStar.find0(new_puzzle.grid)
        self.assertEqual((1, 2), zero_position)

    def test_possible_moves(self):
        moves = AStar.possibleMoves((1, 2))
        expected_moves = [(-1, -0), (0, -1), (1,0)]

        self.assertEqual(expected_moves, moves)

    def test_move_tile(self):
        new_puzzle = Puzzle()
        new_puzzle.grid = [[7, 3, 4], [5, 6, 0], [2, 8, 1]]
        self.assertEqual(True,
                         AStar.compare([[7, 3, 4], [5, 0, 6], [2, 8, 1]], AStar.moveTile(new_puzzle.grid, (0, -1))))
        self.assertEqual(True,
                         AStar.compare([[7, 3, 4], [0, 5, 6], [2, 8, 1]], AStar.moveTile(new_puzzle.grid, (0, -1))))
        self.assertEqual(True,
                         AStar.compare([[7, 3, 4], [2, 5, 6], [0, 8, 1]], AStar.moveTile(new_puzzle.grid, (1, 0))))

    def test_search_hamming(self):
        testPuzzle = Puzzle()
        result : Node = AStar.search(testPuzzle.grid, Hamming.Hamming)
        self.assertEqual(True, AStar.compare([[0, 1, 2], [3, 4, 5], [6, 7, 8]], result.grid))

    def test_search_manhattan(self):
        testPuzzle = Puzzle()
        result = AStar.search(testPuzzle.grid, Manhattan.Manhattan)
        self.assertEqual(True, AStar.compare([[0, 1, 2], [3, 4, 5], [6, 7, 8]], result.grid))


if __name__ == '__main__':
    unittest.main()
