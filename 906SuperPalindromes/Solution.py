from time import time
from math import sqrt, floor, ceil


class Solution:
    def superpalindromesInRange(self, l: str, r: str) -> int:
        return pli(int(l), int(r))


class Palindrom:
    def __init__(self, left: int, rigtht: int):
        self.left = left
        middle = (len(str(left)) + 1) // 2
        end_middle = (len(str(rigtht)) + 1) // 2
        self.start: int = 10 ** (middle - 1)
        self.limit: int = 10 ** end_middle
        self.rigtht: int = rigtht

    def get_pali(self, factor):
        word = str(factor)
        rword = "".join(reversed(word))
        return [int(word + rword), int(word + rword[1:])]

    def get_all(self):
        for factor in range(self.start, self.limit + 1):
            for li in self.get_pali(factor):
                if self.left <= li < self.rigtht:
                    yield li


def pli(l: int, r: int) -> int:
    left = ceil(sqrt(l))
    right = ceil(sqrt(r))
    res = 0
    for n in Palindrom(left, right).get_all():
        if is_palindromes(n * n):
            res += 1
    return res


def is_palindromes(a: int) -> bool:
    a_str = str(a)
    l = len(a_str)
    for index in range(l):
        if a_str[index] != a_str[~index]:
            return False
    return True


if __name__ == "__main__":
    # p = Palindrom(1, 200)
    # for i in p.get_all():
    #     print(i)

    # print((11 + 1) // 2)
    b = time()
    print(Solution().superpalindromesInRange("43143", "7072263972576"))
    # print(Solution().superpalindromesInRange("4", "1000"))
    e = time()
    print(e - b)
    # print(pli(4, 1000))
