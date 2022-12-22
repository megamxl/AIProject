import time
from Puzzle import *
from solvers import Hamming
from solvers import AStar

sT = time.time()
amount = 100

puzzles = [Puzzle() for puzzle in range(amount)]

control = Puzzle([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
toSolve = Puzzle()

AStar.search(toSolve, Hamming)

print(f'{time.time() - sT}s')
