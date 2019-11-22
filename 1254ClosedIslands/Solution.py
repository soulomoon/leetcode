from pprint import pprint
from typing import List


def get_neighbour(vector):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for d in directions:
        yield add_vector(d, vector)


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        self.height = len(grid)
        self.width = len(grid[0])
        self.grid = grid
        closed_sets: List[List[int]] = []

        candidate = set()

        for i, row in enumerate(grid):
            for j, e in enumerate(row):
                if e == 0:
                    candidate.add((i, j))

        # candidate = {(1, 2)}
        while candidate:
            i, j = candidate.pop()
            if closed_set := self.search(i, j):
                closed_sets.append(closed_set)
                candidate = candidate.difference(closed_set)
        # list(map(print, closed_sets))
        return len(closed_sets)

    def search(self, i, j):
        current_set = []
        open_nodes = {(i, j)}
        visited = {(i, j)}
        while open_nodes:
            current = open_nodes.pop()
            current_set.append(current)
            if self.failtest(current):
                return None
            for neighbor in get_neighbour(current):
                # if visited in the passed
                if neighbor in visited:
                    continue
                else:
                    visited.add(neighbor)
                # if fail test return None
                if self.failtest(neighbor):
                    return None
                # if water 1 ignore it
                if self.grid[neighbor[0]][neighbor[1]]:
                    continue
                open_nodes.add(neighbor)
        return current_set

    def failtest(self, neighbor):
        # out of bound for both
        if not (0 <= neighbor[0] < self.height) or not (0 <= neighbor[1] < self.width):
            return True
        # land flow out, it is not island
        if self.grid[neighbor[0]][neighbor[1]] == 0 and \
                (neighbor[0] == 0 or neighbor[1] == 0
                 or neighbor[0] == self.height - 1
                 or neighbor[1] == self.width - 1):
            return True
        return False


def add_vector(x, y):
    return x[0] + y[0], x[1] + y[1]


if __name__ == "__main__":
    # grid = [[1, 1, 1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 0, 1],
    #         [1, 1, 1, 1, 1, 1, 1, 0]]
    grid = [[0, 0, 1, 1, 0, 1, 0, 0, 1, 0], [1, 1, 0, 1, 1, 0, 1, 1, 1, 0], [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
            [0, 1, 1, 0, 0, 0, 0, 1, 0, 1], [0, 0, 0, 0, 0, 0, 1, 1, 1, 0], [0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
            [1, 0, 1, 0, 1, 1, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
            [1, 1, 1, 0, 1, 1, 0, 1, 1, 0]]
    pprint(grid)
    print(Solution().closedIsland(grid))
