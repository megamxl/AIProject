from copy import deepcopy
from queue import PriorityQueue

from DataClasses.Node import Node
from DataClasses.Puzzle import *

# Static initialization of goal state

SOLVE_STATE = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
# All possible moves for a 3x3 2D Grid
MOVES = {'U': (-1, 0), 'L': (0, -1), 'D': (1, 0), 'R': (0, 1)}
REVERSE = {'(-1, 0)': 'U', '(0, -1)': 'L', '(1, 0)': 'D', '(0, 1)': 'R'}


def possibleMoves(zeroCord: tuple) -> list:
    """
    Calculates all possible moves based on the position of the empty tile
    :param zeroCord: Coords of the empty tile
    :return: All possible moves in tuple form (x, y)
    """
    validMoves = []
    for move in MOVES.values():
        newR, newC = zeroCord[0] + move[0], zeroCord[1] + move[1]
        if 0 <= newR <= 2 and 0 <= newC <= 2:
            validMoves.append(move)
    return validMoves


def moveTile(grid: [list, list, list], mv: tuple) -> [list, list, list]:
    """
    Performs a move on the grid based on the tuple
    :param grid: The grid we want to change
    :param mv: The move operation
    :return: The moved grid
    """
    zx, zy = find0(grid)
    grid[zx][zy] = grid[zx + mv[0]][zy + mv[1]]
    grid[zx + mv[0]][zy + mv[1]] = 0
    return grid


def find0(grid: [list, list, list]) -> tuple:
    """
    Finds the 0 in the grid
    :param grid: The grid....
    :return: The coords of 0
    """
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 0: return row, col


def compare(node: list[list, list, list], comp) -> bool:
    """
    compares tow quadratic grid
    :param node: a quadratic grid as list
    :param comp: a quadratic grid as list
    :return:  True or False
    """
    for x in range(len(node)):
        for y in range(len(node)):
            if node[x][y] != comp[x][y]:
                return False
    else:
        return True


def flatten(grid) -> str:
    """
    :param grid: A list
    :return: a String representation of a multi dimensional list
    """
    return ''.join(map(str, grid))


def search(puzzle, heuristic):
    """
    Searches a puzzle bases on a certain heuristic
    :param puzzle: The puzzle we want to solve
    :param heuristic: A given heuristic (Ham. or Man.)
    :return: A solved puzzle Node
    """
    # Initial steps
    pq = PriorityQueue()
    lookedAtStates = set()
    expandedNodes = 0
    addedNodes = 0
    pq.put(Node(puzzle, heuristic.calc(puzzle)))
    lookedAtStates.add(flatten(puzzle))

    # try to find a solution until there are no more possible moves
    while not pq.empty():
        curr_puzzle_state = pq.get()

        # Check if won
        if compare(curr_puzzle_state.grid, SOLVE_STATE):
            return curr_puzzle_state, addedNodes, expandedNodes

        # get all possible moves and derive the depth of the current puzzle
        poss_moves = possibleMoves(find0(curr_puzzle_state.grid))

        # for each new-found move/state copy but not only reference the Puzzle in tmp
        # check if the new created state was already looked at and when not add to priority que
        for move in poss_moves:
            tmp = deepcopy(curr_puzzle_state.grid)
            tmp = moveTile(tmp, move)
            expandedNodes += 1
            # sets only like strings and python only likes str comparison so w e append the str version
            if flatten(tmp) not in lookedAtStates:
                addedNodes += 1
                pq.put(Node(tmp, heuristic.calc(tmp), curr_puzzle_state, move))
                lookedAtStates.add(flatten(tmp))
    return "not found"
