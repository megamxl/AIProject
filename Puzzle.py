import itertools
from copy import deepcopy
from random import *

# Static initialization of goal state
SOLVE_STATE = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]


class Puzzle():
    """
    Serves as a singular 8 Puzzle
    """

    def __init__(self, heuristic=None, grid=None) -> None:
        """
        Creates a 2D 3x3 array with all values == 0
        :param grid: Could optionally be passed to create a pre-defined grid
        """
        if grid is not None:
            self.grid = grid
        else:
            # [0 for _ in range(3)] for _ in range(3)] # Initiates 3x3 Grid with 0s dynamic
            self.grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # Initiates 3x3 Grid with 0s
            # while self.grid
            self.scramble()
            while not self.isSolvable(): self.scramble()
        self.heuristic = heuristic

    def __str__(self) -> str:
        """
        :return: Our 2D 3x3 grid in the form of a multiline string
        """
        s = ""
        for line in self.grid:
            s += f'|{line[0]} {line[1]} {line[2]}|\n'.replace('0', ' ')
        return s

    def __repr__(self) -> str:
        return str(self.grid)

    def scramble(self) -> None:

        """
        Fills our Grid with unique random numbers between 0 - 8
        :return: scrambled grid
        """
        leftNums = [0, 1, 2, 3, 4, 5, 6, 7, 8]  # All possible numbers remaining to fill grid static
        # leftNums = [x for x in range(9)]  # All possible numbers remaining to fill grid
        for rowIndex in range(3):
            for colIndex in range(3):
                # Adds leftNums[randrange] in grid[rowIndex][colIndex]
                self.grid[rowIndex][colIndex] = leftNums.pop(randrange(len(leftNums)))

    def isSolvable(self) -> bool:
        """
        Checks if the current grid is solvable based on the amount of inverses
        :return: True or False if solvable or not
        """
        gridList = sum(self.grid, [])
        inv_count = 0
        for i in range(9):
            for j in range(i + 1, 9):
                # Ignore 0 and check if numbers after gridlist[i] are smaller -> InvNumber for gridlist[i]
                if gridList[j] != 0 and \
                        gridList[i] != 0 and \
                        gridList[i] > gridList[j]:
                    inv_count += 1
        return not bool(inv_count % 2)

    def setGrid(self, grid):
        self.grid = grid
