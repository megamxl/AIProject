import time
from Puzzle import *
from solvers import Manhattan, Hamming
from solvers import AStar


amount = 100

puzzles = [Puzzle() for puzzle in range(amount)]

sT = time.time()
for puzz in puzzles:
    print(AStar.search(deepcopy(puzz.grid), Manhattan))
print(f'Manhattan took {time.time() - sT}s')
sT = time.time()
for puzz in puzzles:
    m= (AStar.search(deepcopy(puzz.grid), Hamming))
    print(m[0],m[2])
print(f'Hamming took {time.time() - sT}s')


control = Puzzle([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
toSolve = Puzzle([[1, 8, 2], [0, 4, 3], [7, 6, 5]])




