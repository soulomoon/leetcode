import heapq
from dataclasses import dataclass
from math import sqrt
from pprint import pprint
from time import time
from typing import List

EMPTY = '.'


@dataclass(frozen=True, eq=True)
class Vect:
    x: int
    y: int

    def __add__(self, other):
        return Vect(self.x + other.x, self.y + other.y)

    def __lt__(self, other):
        return True

    def distant(self, other):
        a = ((self.x - other.x) ** 2) + ((self.y - other.y) ** 2)
        return sqrt(a)


@dataclass(frozen=True, eq=True)
class Node:
    cost: int
    box: Vect
    you: Vect

    def __lt__(self, other):
        return self.cost < other.cost

    def __eq__(self, other):
        return self.box == other.box and self.you == other.you

    def __hash__(self):
        return hash((self.box, self.you))


class Solution:
    def __init__(self):
        self.grid = None
        self.target = None
        self.width = 0
        self.height = 0
        self.result = None

    def set_grid(self, grid):
        self.grid = grid

    def init(self, grid):
        self.grid = grid
        self.height = len(grid)
        self.width = len(grid[0])
        self.target = self.get_location('T')
        self.set_location(self.target, EMPTY)
        self.set_location(self.target, EMPTY)

    def put_node(self, node):
        self.set_location(node.box, 'B')
        self.set_location(node.you, 'S')

    def remove(self) -> Node:
        box = self.get_location('B')
        you = self.get_location('S')
        self.set_location(box, EMPTY)
        self.set_location(you, EMPTY)
        return Node(0, box, you)

    def hueristic(self, node: Node):
        return node.box.distant(self.target)

    def minPushBox(self, grid: List[List[str]]) -> int:
        self.init(grid)
        first = self.remove()
        open_nodes = [(self.hueristic(first), first)]
        visited = {first}
        while open_nodes and not self.result:
            _, current_node = heapq.heappop(open_nodes)
            self.set_location(current_node.box, 'B')
            for new_node in self.expand(current_node):
                if new_node not in visited:
                    visited.add(new_node)
                    if self.gold_reach(new_node):
                        self.result = (new_node.cost, new_node)
                        break
                    else:
                        heapq.heappush(open_nodes, (new_node.cost + self.hueristic(new_node), new_node))
            self.set_location(current_node.box, '.')
        return self.result[0] if self.result else -1

    def gold_reach(self, node: Node):
        return node.box == self.target

    def set_location(self, location: Vect, target: str):
        self.grid[location.x][location.y] = target

    def get_location(self, target: str) -> Vect:
        for x, row in enumerate(self.grid):
            for y, visit in enumerate(row):
                if target == visit:
                    return Vect(x, y)
        raise Exception("Location not found for: " + target)

    def expand(self, node: Node) -> [Node]:
        for a, b in self.expand_vect(node.box):
            if self.reachable(node.you, a):
                yield Node(node.cost + 1, b, node.box)
            if self.reachable(node.you, b):
                yield Node(node.cost + 1, a, node.box)

    def expand_vect(self, vect) -> [(Vect, Vect)]:
        offsets = [(Vect(1, 0), Vect(-1, 0)), (Vect(0, 1), Vect(0, -1))]
        r = []
        for offset in offsets:
            if result := self.get_go_able(vect, offset):
                r.append(result)
        return r

    def get_go_able(self, from_vect: Vect, offsets: (Vect, Vect)) -> (Vect, Vect):
        a = from_vect + offsets[0]
        b = from_vect + offsets[1]
        if self.valid(a) and self.valid(b):
            return a, b
        else:
            return None

    def valid(self, vect: Vect):
        return self.in_bound(vect) and self.grid[vect.x][vect.y] == EMPTY

    def in_bound(self, vect: Vect) -> bool:
        return 0 <= vect.x < self.height and 0 <= vect.y < self.width

    def reachable(self, from_vect: Vect, to: Vect):
        open_nodes = [(from_vect.distant(to), from_vect)]
        close_nodes = set()
        close_nodes.add(from_vect)
        while open_nodes:
            _, vect = heapq.heappop(open_nodes)
            if vect == to:
                return True
            for d_vec in [Vect(1, 0), Vect(0, 1), Vect(-1, 0), Vect(0, -1)]:
                open_node = vect + d_vec
                if open_node not in close_nodes and self.valid(open_node):
                    close_nodes.add(open_node)
                    heapq.heappush(open_nodes, (open_node.distant(to), open_node))
        return False



if __name__ == "__main__":
    # grid = [["#", "#", "#", "#", "#", "#"],
    #         ["#", "T", ".", ".", "#", "#"],
    #         ["#", ".", "#", "B", ".", "#"],
    #         ["#", ".", ".", ".", ".", "#"],
    #         ["#", ".", ".", ".", "S", "#"],
    #         ["#", "#", "#", "#", "#", "#"]]

    # grid = [["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    #         ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#", "#", "#", "#"],
    #         ["#", ".", "#", "#", "#", "#", ".", "#", "#", "#", "#", ".", "#", "#", "#", "."],
    #         ["#", ".", ".", ".", ".", ".", ".", "#", "T", "#", ".", ".", "#", "#", "#", "."],
    #         ["#", ".", ".", ".", "#", ".", ".", ".", ".", ".", ".", ".", "#", "#", "#", "."],
    #         ["#", ".", ".", ".", ".", ".", "B", ".", ".", ".", ".", ".", "#", "#", "#", "."],
    #         ["#", ".", "#", "#", "#", "#", "#", "#", "#", "#", "#", ".", "#", "#", "#", "."],
    #         ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    #         ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    #         ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    #         ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    #         ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    #         ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
    #         ["#", ".", ".", ".", ".", ".", ".", ".", "S", ".", ".", ".", ".", ".", ".", "."],
    #         ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]]

    grid = [["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
            ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#", "#", "#", "#", "#"],
            ["#", ".", ".", ".", "#", "#", "#", "#", ".", "#", "#", "#", "#", ".", "#", "#", "#", ".", "#"],
            ["#", ".", ".", ".", ".", ".", ".", ".", ".", "#", "T", "#", ".", ".", "#", "#", "#", ".", "#"],
            ["#", ".", ".", ".", ".", ".", "#", ".", ".", ".", ".", ".", ".", ".", "#", "#", "#", ".", "#"],
            ["#", ".", "#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#", "#", "#", ".", "#"],
            ["#", ".", "#", ".", "#", "#", "#", "#", "#", "#", "#", "#", "#", ".", "#", "#", "#", ".", "#"],
            ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#", ".", ".", "#"],
            ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#", ".", ".", "#"],
            ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#", ".", ".", "#"],
            ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#", ".", ".", "#"],
            ["#", "#", "#", "#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#", ".", ".", "#"],
            ["#", ".", ".", ".", "#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#", ".", ".", "#"],
            ["#", ".", "B", ".", "#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#", ".", ".", "#"],
            ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#", ".", ".", "#"],
            ["#", ".", ".", "#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#", ".", ".", "#"],
            ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", ".", "#", ".", ".", "#"],
            ["#", ".", ".", ".", ".", ".", ".", ".", ".", ".", "S", ".", ".", ".", ".", "#", ".", ".", "#"],
            ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]]
    s = Solution()
    b = time()
    pprint(s.minPushBox(grid))
    e = time()
    print(e - b)

    # s.init(grid)
    # s.remove()
    # for node in (list(s.expand(Node(box=Vect(x=2, y=3), you=Vect(x=4, y=4))))):
    #     s.put_node(node)
    #     print(node)
    #     pprint(s.grid)
    #     s.remove()

    # pprint(s.grid)
