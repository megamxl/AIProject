import time
from Puzzle import *

sT = time.time()
amount = 100_000

puzzles = [Puzzle() for puzzle in range(amount)]
print(time.time() - sT)
