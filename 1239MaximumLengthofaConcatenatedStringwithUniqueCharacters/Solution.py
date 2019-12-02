from typing import List, Set


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        return maxLength(arr, set())


def maxLength(arr: List[str], seen: Set):
    if not arr:
        return 0
    elif len(set(arr[0])) == len(arr[0]) and seen.isdisjoint(arr[0]):
        return max(maxLength(arr[1:], seen.union(arr[0])) + len(arr[0]), maxLength(arr[1:], seen))
    else:
        return maxLength(arr[1:], seen)




if __name__ == "__main__":
    # arr = ["un", "iq", "ue"]
    arr = ["cha", "r", "act", "ers"]
    print(Solution().maxLength(arr))
