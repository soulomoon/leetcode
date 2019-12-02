from math import sqrt, inf
from time import time
from typing import List


# a cheated method full of special case
class Solution:
    def tilingRectangle(self, n: int, m: int) -> List[int]:
        return self.solve(n, m)

    def solve(self, n: int, m: int) -> List[int]:
        if n < m:
            return self.solve(m, n)
        self.rez = inf

        ssu = square_sum_up(m * n)

        def dp(skyline: List[int], count, left):
            if ssu[left] + count >= self.rez:
                return
            ground = min(skyline)
            if ground >= n:
                # print(n, skyline)
                self.rez = min(count, self.rez)
                return
            begin = skyline.index(ground)
            size_limit = 1
            while ground + size_limit < n \
                    and begin + size_limit < m \
                    and skyline[begin + size_limit] == ground:
                size_limit += 1
            # print(skyline, ground, begin, size_limit, count)
            for size in range(size_limit, 0, -1):
                new_skyline = list(skyline)
                for index in range(begin, begin + size):
                    new_skyline[index] += size
                dp(new_skyline, count + 1, left - size ** 2)

        dp([0] * m, 0, m * n)
        return self.rez


def square_sum_up(limit):
    dp = [-1] * (limit + 1)
    dp[0] = 0
    for i in range(1, limit + 1):
        dp[i] = 1 + min(dp[i - j ** 2] for j in range(1, 1 + int(sqrt(i))))
    return dp


if __name__ == "__main__":
    t = time()
    print(Solution().solve(2, 3))
    # print(Solution().tilingRectangle(2, 3))
    print(Solution().solve(11, 13))
    # print(Solution().tilingRectangle(11, 13))
    # print(squres_sum_up(143))
    # pprint(Solution().tilingRectangle(5, 8))
    te = time()
    print(te - t)
