from collections import deque
from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        counter = 0
        con = deque()
        con.append(-1)
        for i, n in enumerate(nums):
            if n % 2 == 1:
                counter += 1
                con.append(i)
                if counter > k:
                    left = con.popleft()
                    left_range = con[0] - left
                    right_range = con[-1] - con[-2]
                    res += left_range * right_range
        if counter >= k:
            left_range = con[1] - con[0]
            right_range = len(nums) - con[-1]
            res += left_range * right_range
        return res


if __name__ == "__main__":
    x = [2, 2, 2, 1, 2, 2, 1, 2, 2, 2]
    y = 2
    print(Solution().numberOfSubarrays(x, y))
