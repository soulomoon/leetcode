from typing import List


class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        res = []
        tmp = []
        cur = None
        for index, e in enumerate(tree):
            if not cur or cur[0] != e:
                if cur:
                    tmp.append(cur)
                cur = e, 1
            else:
                cur = e, cur[1] + 1
        if cur:
            tmp.append(cur)

        left = None
        right = None
        for e in tmp:
            if not left:
                left = e
            elif not right:
                left = (left[0], e[0]), left[1] + e[1]
                right = e
            else:
                # uedate if new one is here
                if e[0] not in left[0]:
                    res.append(left[1])
                    left = (right[0], e[0]), right[1] + e[1]
                else:
                    left = left[0], left[1] + e[1]
                right = e
        res.append(left[1])
        return max(res) if res else 0

    def find_longest(self, index, tmp):
        left = tmp[index][0]
        if len(tmp) <= index + 1:
            return tmp[index][1]
        right = tmp[index + 1][0]
        r = 0
        for index in range(index, len(tmp)):
            if tmp[index][0] == left or tmp[index][0] == right:
                r += tmp[index][1]
            else:
                return r
        return r


if __name__ == "__main__":
    tree = [1, 2, 1]
    print(Solution().totalFruit(tree))
