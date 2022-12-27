import collections

from Node import Node
from Puzzle import *
from solvers import Manhattan, Hamming
import math

# All possible moves for a 3x3 2D Grid
MOVES = {'U': (-1, 0), 'L': (0, -1), 'D': (1, 0), 'R': (0, 1)}
DEF_VALUE = math.inf


class AStar:

    def __init__(self, start) -> None:
        self.start = start

    def solve(self):
        """
        Searches a puzzle bases on a certain heuristic
        :param puzzle: The puzzle we want to solve
        :param heuristic: A given heuristic (Ham. or Man.)
        :return: A solved puzzle
        """
        queue = collections.deque([Node(self.start)])
        print(list(queue))
        visited = set()
        visited.add(queue[0].state())
        print(visited)
        while queue:
            queue = collections.deque(sorted(list(queue), key=lambda node: node.f))
            node = queue.popleft()
            if node.solved:
                print(node.puzzle)
                return node.path

            for move, action in node.actions:
                child = Node(move(), node, action)

                if child.state not in visited:
                    queue.appendleft(child)
                    visited.add(child.state)


p1 = Puzzle(Hamming, [[1, 2, 3], [4, 5, 0], [6, 7, 8]])
aStar = AStar(p1)
p = aStar.solve()
print(p)

# steps = 0
# for node in p:
#     print(node.action)
#     print(node)
#     steps += 1

# print("Total number of steps: " + str(steps))
# print(possibleMoves((0, 0), 'U'))
# print(find0([[4, 1, 2], [0, 3, 5], [6, 7, 8]]))
# print(moveTile([[4, 1, 2], [0, 3, 5], [6, 7, 8]], (0, 1)))
