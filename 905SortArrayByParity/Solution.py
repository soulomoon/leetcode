from typing import List


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        return A.sort(key=lambda x: x % 2)
