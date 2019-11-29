from typing import List


class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        return [start ^ grey_code(i) for i in range(2 ** n)]

    def circularPermutation_slow(self, n: int, start: int) -> List[int]:

        # lst = get_standard(n)
        lst = [0]
        a = 0
        b = 1
        for i in range(n):
            new_lst = []
            for e in lst:
                a, b = b, a
                new_lst.append(a + e)
                new_lst.append(b + e)
            lst = new_lst
            a = a * 2
            b = b * 2
        index = lst.index(start)
        return lst[index:] + lst[:index]


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


def grey_code(n):
    return n ^ (n >> 1)


if __name__ == "__main__":
    print(1 >> 1)
    print(2 >> 1)
    print((7 >> 1))
    print(7 ^ (7 >> 1))
    # print(g(1))
    # print(g(2))
    # print(g(3))
    # print(g(4))
    # print(g(5))

    print(Solution().circularPermutation(3, 2))
