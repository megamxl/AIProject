from random import *


class Puzzle():
    def __init__(self) -> None:
        """
        Creates a 2D 3x3 array with all values == 0
        """
        self.grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # Initiates 3x3 Grid with 0s
        # [0 for _ in range(3)] for _ in range(3)] # Initiates 3x3 Grid with 0s
        self.scramble()

    def __str__(self) -> str:
        """
        :return: Our 2D 3x3 grid in the form of a multiline string
        """
        s = ""
        for line in self.grid:
            for num in line:
                s += str(num) + ' '
            s += '\n'
        return s

    def scramble(self):
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
