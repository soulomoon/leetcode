from math import inf
from typing import List

direction = [(1, 0), (0, 1), (0, -1), (-1, 0), (0, 0)]


class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        height = len(mat)
        width = len(mat[0])
        n = height * width
        mini = inf
        mat_number = 0
        for row in mat:
            for x in row:
                mat_number <<= 1
                mat_number += x

        def op(x, y, mn):
            for a, b in direction:
                nx = a + x
                ny = b + y
                if width > nx >= 0 and height > ny >= 0:
                    mn ^= 1 << (n - (ny * width + nx + 1))
            return mn

        def genmap():
            for y in range(height):
                for x in range(width):
                    yield op(x, y, 0)

        lst = list(genmap())

        for code in range(2 ** n):
            mn = mat_number
            count = 0
            for i in range(n):
                if 0X1 << i & code:
                    mn ^= lst[i]
                    count += 1
            if mn == 0:
                mini = min(mini, count)
        return mini if mini != inf else -1


if __name__ == "__main__":
    # mat = [[0, 0], [0, 1]]
    mat = [[1, 0, 0], [1, 0, 0]]
    print(Solution().minFlips(mat))
