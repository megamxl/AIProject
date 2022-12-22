from Puzzle import *
from queue import PriorityQueue
from collections import defaultdict

# Static initialization of goal state
SOLVE_STATE = Puzzle([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
# All possible moves for a 3x3 2D Grid
MOVES = {'U': (-1, 0), 'L': (0, -1), 'D': (1, 0), 'R': (0, 1)}


def possibleMoves(zeroCord: tuple, lastMove: chr):
    """
    Calculates all possible moves based on the position of the empty tile
    :param zeroCord: Coords of the empty tile
    :param lastMove: U, L, D, R to access the move
    :return: All possible moves in tuple form (x, y)
    """
    validMoves = []
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

def search(puzzle: Puzzle, heuristic) -> Puzzle:
    """
    Searches a puzzle bases on a certain heuristic
    :param puzzle: The puzzle we want to solve
    :param heuristic: A given heuristic (Ham. or Man.)
    :return: A solved puzzle
    """
    pq = PriorityQueue()
    searchTree = defaultdict()
    gScore = defaultdict()
    # Start State
    gScore['0'] = puzzle
    fScore = defaultdict()
    fScore['n0'] = heuristic.calc(puzzle)

    print(gScore.values())
    print(fScore.values())

    while not pq.empty():
        print('Tacocat')
        break

    return SOLVE_STATE


# print(possibleMoves((0, 0), 'U'))
# print(find0([[4, 1, 2], [0, 3, 5], [6, 7, 8]]))
# print(moveTile([[4, 1, 2], [0, 3, 5], [6, 7, 8]], (0, 1)))
