from typing import List


class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        lst = get_standard(n)
        print(lst)
        r = lst
        index = r.index(start)
        return r[index:] + r[:index]


def get_standard(n: int) -> [int]:
    if n == 1:
        return [0, 1]
    else:
        child = get_standard(n - 1)
        new = []
        a = 0
        b = 2 ** (n - 1)
        for s in child:
            a, b = b, a
            new.append(a + s)
            new.append(b + s)
        return new


if __name__ == "__main__":
    print(Solution().circularPermutation(3, 2))
