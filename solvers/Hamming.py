import Puzzle


def calc(puzzle: list[list, list, list]) -> int:
    """
     This function solves the Puzzle based on Hamming heuristic
    :param puzzle: The unsolved puzzle
    :return: The solved puzzle
    """
    sum, counter = 0, 0
    for row in puzzle:
        for col in row:
            if col != counter and col != 0:
                sum += 1
            counter +=1
    return sum
