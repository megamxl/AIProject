import time
from Puzzle import *
from solvers import Manhattan
from solvers import AStar

sT = time.time()
amount = 100

puzzles = [Puzzle() for puzzle in range(amount)]

control = Puzzle([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
toSolve = Puzzle([[7, 3, 4], [5, 6, 0], [2, 8, 1]])

# AStar.search(toSolve, Hamming)
print(toSolve)
print(Manhattan.calc(toSolve))

print(f'{time.time() - sT}s')
