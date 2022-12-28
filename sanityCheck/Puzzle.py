import itertools
import random


class Puzzle:
    """
    A class representing an '8-puzzle'.
    - 'board' should be a square list of lists with integer entries 0...width^2 - 1
       e.g. [[1,2,3],[4,0,6],[7,5,8]]
    """

    def __init__(self, grid):
        self.width = len(grid[0])
        self.grid = grid

    @property
    def solved(self):
        """
        The puzzle is solved if the flattened board's numbers are in
        increasing order from left to right and the '0' tile is in the
        first position on the board
        """
        N = self.width * self.width
        return str(self) == ''.join(map(str, range(0, N)))
        # return str(self) == ''.join(map(str, range(1, N))) + '0'

    @property
    def actions(self):
        """
        Return a list of 'move', 'direction' pairs. 'move' can be called
        to return a new puzzle that results in sliding the '0' tile in
        the direction of 'direction'.
        """

        def create_move(at, to):
            return lambda: self._move(at, to)

        moves = []
        for i, j in itertools.product(range(self.width), range(self.width)):
            direcs = {'R': (i, j - 1),
                      'L': (i, j + 1),
                      'D': (i - 1, j),
                      'U': (i + 1, j)}

            for direction, (row, col) in direcs.items():
                if 0 <= row < self.width and 0 <= col < self.width and \
                        self.grid[row][col] == 0:
                    move = create_move((i, j), (row, col)), direction
                    moves.append(move)
        # print(moves)
        return moves

    @property
    def manhattan(self):
        """

        :return:
        """
        distance = 0
        for rowIndex in range(3):
            for colIndex in range(3):
                if self.grid[rowIndex][colIndex] != 0:

                    # TODO: Fehler in Manhattan -> -1 sorgt dafür das 1 an 1. Stelle
                    row, col = divmod(self.grid[rowIndex][colIndex], self.width)
                    # print(row, col)
                    distance += abs(row - rowIndex) + abs(col - colIndex)
        return distance

    @property
    def hamming(self):
        return len([x for x in range(self.width * self.width) if self.grid[x // 3][x % 3] == x])

    def shuffle(self):
        """
        Return a new puzzle that has been shuffled with 1000 random moves
        """
        puzzle = self
        for _ in range(1000):
            puzzle = random.choice(puzzle.actions)[0]()
        return puzzle

    def copy(self):
        """
        Return a new puzzle with the same board as 'self'
        """
        board = []
        for row in self.grid:
            board.append([x for x in row])
        return Puzzle(board)

    def _move(self, at, to):
        """
        Return a new puzzle where 'at' and 'to' tiles have been swapped.
        NOTE: all moves should be 'actions' that have been executed
        """
        copy = self.copy()
        i, j = at
        r, c = to
        copy.grid[i][j], copy.grid[r][c] = copy.grid[r][c], copy.grid[i][j]
        return copy

    def pprint(self):
        s = ""
        for l in self.grid:
            s += f'|{l[0]} {l[1]} {l[2]}|\n'.replace('0', ' ')
        print(s)

    def __str__(self):
        return ''.join(map(str, self))

    def __iter__(self):
        """
        We need this so we can map over ourselves in __str__
        :return: A new iterable that provides each row of the grid ^^
        """
        for row in self.grid:
            yield from row