import time
from Puzzle import *
from solvers import Manhattan, Hamming
from solvers import AStar


amount = 100

puzzles = [Puzzle() for puzzle in range(amount)]

sT = time.time()

curPuzzle = 1
for puzz in puzzles:
    print(curPuzzle)
    AStar.search(deepcopy(puzz.grid), Manhattan)
    curPuzzle += 1
print(f'Manhattan took {time.time() - sT}s')

sT = time.time()

curPuzzle = 1
for puzz in puzzles:
    print(curPuzzle)
    AStar.search(deepcopy(puzz.grid), Hamming)
    curPuzzle += 1

print(f'Hamming took {time.time() - sT}s')


control = Puzzle([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
toSolve = Puzzle([[1, 8, 2], [0, 4, 3], [7, 6, 5]])




