from math import inf
from typing import List


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        v = cal_v(coordinates[0], coordinates[1])
        for i in range(1, len(coordinates) - 1):
            if cal_v(coordinates[i], coordinates[i + 1]) != v:
                return False
        return True


def cal_v(x, y):
    if (x[1] - y[1]) == 0:
        return inf
    return (x[0] - y[0]) / (x[1] - y[1])
