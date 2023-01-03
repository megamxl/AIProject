import math

from AIProject.Heuristics.HeuristicInterface import HeuristicInterface

class Euclidean(HeuristicInterface):
    def calc(puzzle) -> int:
        """
         This function solves the Puzzle based on Euclidian heuristic
        :param puzzle: The unsolved puzzle
        :return: The solved puzzle
        """
        distance = 0
        for x in range(3):
            for y in range(3):
                puzNum = puzzle[x][y]
                if puzNum == 0: continue
                row = puzNum // 3
                col = puzNum % 3
                distance += math.sqrt((math.pow((row - x), 2))) + math.sqrt((math.pow((col - y), 2)))
        return distance
