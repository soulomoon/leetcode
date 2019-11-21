from typing import List


class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        k = colsum.count(1)
        n = colsum.count(2)
        upper -= n
        lower -= n
        if upper < 0 and lower < 0 and k != upper + lower:
            return []
        upper_list = [0] * len(colsum)
        lower_list = [0] * len(colsum)

        for i, s in enumerate(colsum):
            if s == 2:
                upper_list[i] = 1
                lower_list[i] = 1
            elif s == 1:
                if upper:
                    upper -= 1
                    upper_list[i] = 1
                elif lower:
                    lower -= 1
                    lower_list[i] = 1
        return [upper_list, lower_list]


if __name__ == "__main__":
    Solution().reconstructMatrix(9, 2, [0, 1, 2, 0, 0, 0, 0, 0, 2, 1, 2, 1, 2])
