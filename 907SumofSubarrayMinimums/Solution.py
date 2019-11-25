import heapq
from typing import List

m = (10 ** 9) + 7


def get_count_both(A, r=True):
    stack = []
    res = [0 for _ in A]
    cpm = (lambda a, b: a < b) if r else (lambda a, b: a <= b)

    def feed(right_end):
        old_idx = stack.pop()
        left = old_idx - (stack[-1] if stack else -1)
        right = right_end - old_idx
        res[old_idx] = right * left

    for idx, e in enumerate(A):
        while stack and cpm(e, A[stack[-1]]):
            feed(idx)
        stack.append(idx)
    while stack:
        feed(len(A))
    return res


class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        count = get_count_both(A)
        s = 0
        for k, c in enumerate(count):
            s = (s + c * A[k]) % m
        return s


def show(A: List[int]) -> int:
    matrix: List[List] = []
    for i in range(len(A)):
        row = []
        for _ in range(len(A) - i):
            row.append(None)
        matrix.append(row)

    for i in range(len(A)):
        matrix[i][0] = A[i]

    for i in range(len(A)):
        for j in range(1, len(A) - i):
            matrix[i][j] = min(matrix[i][j - 1], A[i + j])
    for i, row in enumerate(matrix):
        print("   " * i, row)

    return sum(sum(i for i in row) for row in matrix)


if __name__ == "__main__":
    # A = [3, 2, 5, 6, 7, 4, 1]
    A = [3, 1, 2, 4]
    # A = [71, 55, 82, 55]
    print(get_count_both(A))
    # print(show(A))
    # show(list(reversed(A)))
    print(Solution().sumSubarrayMins(A))
