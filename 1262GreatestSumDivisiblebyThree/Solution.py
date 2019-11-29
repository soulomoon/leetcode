from typing import List


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        sum_nums = sum(nums)
        print("sum", sum_nums)
        # remains
        remain = sum_nums % 3
        # if 0 return it
        if remain == 0:
            return sum_nums
        # for various mod list
        dct = {}
        # smallest first
        nums.sort()
        for i in range(1, 3):
            dct[i] = []

        # get those remains 1 and 2
        for i in nums:
            m = i % 3
            if m != 0:
                dct[m].append(i)

        if remain == 2 and len(dct[1]) > 1 and dct[2]:
            if dct[1][0] + dct[1][1] < dct[2][0]:
                return sum_nums - dct[1][0] - dct[1][1]
            else:
                return sum_nums - dct[2][0]
        elif remain == 1 and len(dct[2]) > 1 and dct[1]:
            if dct[2][0] + dct[2][1] < dct[1][0]:
                return sum_nums - dct[2][0] - dct[2][1]
            else:
                return sum_nums - dct[1][0]
        elif dct[remain]:
            return sum_nums - dct[remain][0]
        else:
            return 0


if __name__ == "__main__":
    print(19 % 3)
    print(2 % 3)
    print(Solution().maxSumDivThree([2, 6, 2, 2, 7]))
