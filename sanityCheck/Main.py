import time

from sanityCheck.Puzzle import Puzzle
from sanityCheck.Solver import Solver

# example of use
board = [[1, 0, 2], [6, 4, 3], [7, 8, 5]]
puzzle = Puzzle(board)
# puzzle = puzzle.shuffle()
s = Solver(puzzle)
tic = time.perf_counter()
p = s.solve()
toc = time.perf_counter()

steps = 0
for node in p:
    print(node.action)
    node.puzzle.pprint()
    steps += 1

print("Total number of steps: " + str(steps))
print("Total amount of time in search: " + str(toc - tic) + " second(s)")

# for x in range(9):
#     print(divmod(x, 3))