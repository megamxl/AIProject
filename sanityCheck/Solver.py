import collections

from sanityCheck.Node import Node


class Solver:
    """
    An '8-puzzle' solver
    - 'start' is a Puzzle instance
    """

    def __init__(self, start):
        self.start = start

    def solve(self):
        """
        Perform breadth first search and return a path
        to the solution, if it exists
        """
        steps = 0
        queue = collections.deque([Node(self.start)])
        visited = set()
        visited.add(queue[0].state)
        while queue:
            steps += 1
            queue = collections.deque(sorted(list(queue), key=lambda node: node.f))
            node = queue.popleft()
            if node.solved:
                print(f"Explored Paths: {steps}")
                return node.path

            # move = function to move puzzle, action (U,L,D,R)
            for move, action in node.actions:
                child = Node(move(), node, action)

                if child.state not in visited:
                    queue.appendleft(child)
                    visited.add(child.state)