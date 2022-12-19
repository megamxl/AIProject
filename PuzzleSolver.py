from copy import deepcopy

from Puzzle import Puzzle
from solvers import AStar, BranchAndBound, Hamming, Manhattan

amount = 100
puzzles = [Puzzle() for puzzle in range(amount)]

for puzzle in puzzles:
    aSol = AStar.solve(deepcopy(puzzle))
    bSol = BranchAndBound.solve(deepcopy(puzzle))
    cSol = Hamming.solve(deepcopy(puzzle))
    dSol = Manhattan.solve(deepcopy(puzzle))
