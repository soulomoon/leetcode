from math import gcd
from typing import List


class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        if len(nums) < 1:
            return False
        current = nums[0]
        for n in nums[1:]:
            current = gcd(current, n)
        return current == 1
