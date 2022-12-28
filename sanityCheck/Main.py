import time

from sanityCheck.Puzzle import Puzzle
from sanityCheck.Solver import Solver

# example of use
board = [[7, 2, 4], [5, 0, 6], [8, 3, 1]]
# board = [[1, 8, 2], [0, 4, 3], [7, 6, 5]]
# board = [[1, 2, 5], [3, 7, 4], [6, 0, 8]]
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