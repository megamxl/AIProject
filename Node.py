from Puzzle import *


class Node:
    """
    This helps us work with the A* Queue, so we can sort properly :3
    """

    def __init__(self, puzzle: Puzzle, parent=None, move=None) -> None:
        self.puzzle = puzzle,
        self.parent = parent,
        self.move = move
        if self.parent is None:
            self.g = parent.g + 1
        else:
            self.g = 0

    @property
    def score(self):
        return self.g + self.h

    @property
    def state(self):
        """
        Return a hashable representation of self
        """
        return str(self)

    @property
    def path(self):
        node, p = self, []
        while node:
            p.append(node)
            node = node.parent
        yield from reversed(p)

    @property
    def solved(self):
        return self.puzzle.isSolved()

    @property
    def moves(self):
        return self.puzzle.moves

    @property
    def h(self):
        """"h"""
        return self.puzzle.heuristic.calc()

    @property
    def f(self):
        return self.h + self.g

    def __str__(self):
        return str(self.puzzle.__str__())

    def __repr__(self) -> str:
        return f"Grid: {self.puzzle}, Parent: {self.parent}, f: {self.f}"


