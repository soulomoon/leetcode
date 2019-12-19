from math import inf
from typing import List

direction = [(1, 0), (0, 1), (0, -1), (-1, 0), (0, 0)]


class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        height = len(mat)
        width = len(mat[0])
        n = height * width
        mini = inf

        def op(x, y):
            for a, b in direction:
                nx = a + x
                ny = b + y
                if width > nx >= 0 and height > ny >= 0:
                    matcp[ny][nx] ^= 1

        for code in range(2 ** n):
            matcp = [row.copy() for row in mat]
            count = 0
            for i in range(n):
                if 0X1 << i & code:
                    op(i % width, i // width)
                    count += 1
            if all(all(i == 0 for i in row) for row in matcp):
                mini = min(mini, count)
        return mini if mini != inf else -1


if __name__ == "__main__":
    mat = [[0, 0], [0, 1]]
    print(Solution().minFlips(mat))
