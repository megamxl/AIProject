from copy import deepcopy

from Puzzle import *
from queue import PriorityQueue
from collections import defaultdict

# Static initialization of goal state
from solvers import Hamming, Manhattan

SOLVE_STATE = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
# SOLVE_STATE = [[1, 2, 3], [4, 5, 5], [7, 8, 0]]
# All possible moves for a 3x3 2D Grid
MOVES = {'U': (-1, 0), 'L': (0, -1), 'D': (1, 0), 'R': (0, 1)}


class Node:
    def __init__(self, puzzle, parent=None, move=None, depth=None) -> None:
        self.puzzle = puzzle,
        self.parent = parent,
        self.move = move
        self.depth =depth


def possibleMoves(zeroCord: tuple, lastMove=None):
    """
    Calculates all possible moves based on the position of the empty tile
    :param zeroCord: Coords of the empty tile
    :param lastMove: U, L, D, R to access the move
    :return: All possible moves in tuple form (x, y)
    """
    validMoves = []
    inv_move = ''
    if lastMove is not None:
        mv = MOVES[lastMove]
        inv_move = tuple(x * -1 for x in mv)
    for move in MOVES.values():
        if move == inv_move: continue
        newR, newC = zeroCord[0] + move[0], zeroCord[1] + move[1]
        if 0 <= newR <= 2 and 0 <= newC <= 2: validMoves.append(move)
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
            if grid[row][col] == 0: return tuple((row, col))


def compare(grid, comp):
    for x in range(len(grid)):
        for y in range(len(grid)):
            if grid[x][y] != comp[x][y]:
                return False
    else:
        return True


def search(puzzle, heuristic) -> Puzzle:
    """
    Searches a puzzle bases on a certain heuristic
    :param puzzle: The puzzle we want to solve
    :param heuristic: A given heuristic (Ham. or Man.)
    :return: A solved puzzle
    """
    pq = PriorityQueue()
    lookedAtStates = set()
    steps = 0
    # Priority # GridState # Depth as String
    pq.put((0, puzzle, str(0)))
    lookedAtStates.add(str(puzzle))
    while not pq.empty():
        steps += steps + 1
        curr_puzzle_state = pq.get()

        # Check if won
        if compare(curr_puzzle_state[1], SOLVE_STATE):
            return (curr_puzzle_state[1], steps, curr_puzzle_state[2])
        # Counter for overall steps


        # get all possible moves and derive the depth of the current puzzle
        poss_moves = possibleMoves(find0(curr_puzzle_state[1]))
        cur_dept = int(curr_puzzle_state[2])

        # for each new-found move/state copy but not only reference the Puzzle in tmp
        # check if the new created state was already looked at and when not add to priority que
        for move in poss_moves:
            tmp = deepcopy(curr_puzzle_state[1])
            tmp = moveTile(tmp, move)
            if str(tmp) not in lookedAtStates:
                pq.put((heuristic.calc(tmp) + cur_dept + 1, tmp, str(cur_dept + 1)))
                lookedAtStates.add(str(tmp))
    return "not found"

# print(possibleMoves((0, 0), 'U'))
p = Puzzle()
print(p)
# print(search([[1, 0, 2], [6, 4, 3], [7, 8, 5]], Manhattan))
print(search([[7, 1, 0], [3, 5, 2], [4, 8, 6]], Hamming))
print(search([[7, 1, 0], [3, 5, 2], [4, 8, 6]], Manhattan))
#print(search(p.grid, Manhattan))
# print(moveTile([[4, 1, 2], [0, 3, 5], [6, 7, 8]], (0, 1)))
