class Node:
    """
    This helps us work with the A* Queue, so we can sort properly :3
    """

    def __init__(self, grid: list[list, list, list], h: int, parent=None, move=None) -> None:
        self.grid = grid
        self.parent = parent
        self.move = move
        self.h = h
        # through this class approach we can handle the depth of the move without counting and subtracting in A*
        if self.parent is not None:
            self.g = parent.g + 1
        else:
            self.g = 0

        self.f = self.calcF()

    # is the heuristic formular of a* f(x) = h(x) + g(x)
    def calcF(self):
        return self.h + self.g

    # through the parent structure as list we can traverse the Way from the bottom (solvestate) Up
    def getPath(self):
        node, p = self, []
        while node:
            p.append(node)
            node = node.parent
        yield from reversed(p)

    # For pythons priority queue to sort this object
    def __lt__(self, other):
        return self.f < other.f

    # representing the node as string for print
    def __str__(self) -> str:
        s = ""
        for line in self.grid:
            s += f'|{line[0]} {line[1]} {line[2]}|\n'.replace('0', ' ')
        return s

    # representing the node as string for troubleshoot purposes
    def __repr__(self) -> str:
        return f"Grid: {' '.join(map(str, self.grid))} F: {self.f} Moves: {self.move}"
