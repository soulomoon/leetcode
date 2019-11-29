from itertools import chain
from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        cs = chain(*grid)
        result = [0] * (n * m)
        for index, e in enumerate(cs):
            result[(index + k) % (n * m)] = e
        return list(map(list, zip(*[iter(result)] * m)))



if __name__ == "__main__":
    # grid = [[1, 3, 4], [2, 4, 3]]
    result = Solution().shiftGrid(grid, k)
    print(result)
