import time
from Puzzle import *

sT = time.time()
amount = 10_000

puzzles = [Puzzle() for puzzle in range(amount)]
print(f'{time.time() - sT}s')
