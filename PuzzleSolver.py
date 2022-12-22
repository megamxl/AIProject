from copy import deepcopy

from Puzzle import Puzzle
from solvers import AStar, BranchAndBound, Hamming, Manhattan

amount = 100
puzzles = [Puzzle() for puzzle in range(amount)]
