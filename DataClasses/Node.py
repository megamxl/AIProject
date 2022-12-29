class Node:
    """
    This helps us work with the A* Queue, so we can sort properly :3
    """

    def __init__(self, grid: list[list, list, list], h: int, parent=None, move=None) -> None:
        self.grid = grid
        self.parent = parent
        self.move = move
        self.h = h
        if self.parent is not None:
            self.g = parent.g + 1
        else:
            self.g = 0

        self.f = self.calcF()

    def calcF(self):
        return self.h + self.g

    def getPath(self):
        node, p = self, []
        while node:
            p.append(node)
            node = node.parent
        yield from reversed(p)

    def __lt__(self, other):
        return self.f < other.f

    def __str__(self) -> str:
        s = ""
        for line in self.grid:
            s += f'|{line[0]} {line[1]} {line[2]}|\n'.replace('0', ' ')
        return s

    def __repr__(self) -> str:
        return f"Grid: {' '.join(map(str, self.grid))} F: {self.f} Moves: {self.move}"
