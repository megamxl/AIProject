from Puzzle import *


def calc(puzzle: Puzzle) -> int:
    """
     This function solves the Puzzle based on Manhattan heuristic
    :param puzzle: The unsolved puzzle
    :return: The solved puzzle
    """
    distance = 0
    for x in range(3):
        for y in range(3):
            puzNum = puzzle.grid[x][y]
            if puzNum == 0: continue
            row = puzNum // 3
            col = puzNum % 3
            distance += abs(row - x) + abs(col - y)
    return distance
