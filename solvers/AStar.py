from Node import Node
from Puzzle import *
from queue import PriorityQueue

# Static initialization of goal state
from solvers import Hamming, Manhattan

SOLVE_STATE = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
# All possible moves for a 3x3 2D Grid
MOVES = {'U': (-1, 0), 'L': (0, -1), 'D': (1, 0), 'R': (0, 1)}
Reverse = {'(-1, 0)': 'U', '(0, -1)': 'L' , '(1, 0)': 'D' , '(0, 1)':'R'}


def possibleMoves(zeroCord: tuple):
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
            if grid[row][col] == 0: return tuple((row, col))


def compare(node: list[list, list, list], comp):
    for x in range(len(node)):
        for y in range(len(node)):
            if node[x][y] != comp[x][y]:
                return False
    else:
        return True


def flatten(grid):
    return ''.join(map(str, grid))


def search(puzzle, heuristic) -> Node:
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
    pq.put(Node(puzzle, heuristic.calc(puzzle)))
    # pq.put((0, puzzle, str(0)))
    lookedAtStates.add(flatten(puzzle))
    while not pq.empty():
        # print(pq.queue)
        steps += 1
        curr_puzzle_state = pq.get()

        # Check if won
        if compare(curr_puzzle_state.grid, SOLVE_STATE):
            return curr_puzzle_state
        # Counter for overall steps

        # get all possible moves and derive the depth of the current puzzle
        poss_moves = possibleMoves(find0(curr_puzzle_state.grid))
        cur_dept = curr_puzzle_state.g

        # for each new-found move/state copy but not only reference the Puzzle in tmp
        # check if the new created state was already looked at and when not add to priority que
        for move in poss_moves:
            tmp = deepcopy(curr_puzzle_state.grid)
            tmp = moveTile(tmp, move)
            if flatten(tmp) not in lookedAtStates:
                pq.put(Node(tmp, heuristic.calc(tmp), curr_puzzle_state, move))
                # (heuristic.calc(tmp) + cur_dept + 1, tmp, str(cur_dept + 1)))
                lookedAtStates.add(flatten(tmp))
    return "not found"


# print(possibleMoves((0, 0), 'U'))
# p = Puzzle()
# # pr
# endNode: Node = search(p.grid, Manhattan)
# for x in endNode.getPath():
#     print("m->" + str(Reverse.get(str(x.move))))
#     print(x)


# print(search([[7, 1, 0], [3, 5, 2], [4, 8, 6]], Hamming))
# print(search([[7, 1, 0], [3, 5, 2], [4, 8, 6]], Manhattan))
# print(search(p.grid, Manhattan))
# print(moveTile([[4, 1, 2], [0, 3, 5], [6, 7, 8]], (0, 1)))
