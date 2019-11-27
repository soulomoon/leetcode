import time
from typing import List

m = (10 ** 9) + 7


class Solution:
    def sumSubseqWidths(self, A: List[int]) -> int:
        A.sort()
        s = 0
        lower = 1
        for i, e in enumerate(A):
            s = (s + lower * (e - A[~i])) % m
            lower = (lower * 2) % m
        return s


if __name__ == "__main__":
    # A = [3, 2, 5, 6, 7, 4, 1]
    # A = [3, 1, 2, 4]
    A = [2, 1, 3]

    # A = [71, 55, 82, 55]
    # print(get_count_both(A))
    # print(show(A))
    # show(list(reversed(A)))
    start_time = time.time()
    print(Solution().sumSubseqWidths(A))
    end_time = time.time()
    print("time:", end_time - start_time)
    print((-m - 1) // 2 % m)
    print(((-m - 1) % m) // 2)
    print(~1)
    print(1)
