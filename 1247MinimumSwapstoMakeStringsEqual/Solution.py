from dataclasses import dataclass
from math import inf
from typing import Set, Dict, Optional, Deque
from collections import deque, Counter


class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        x_count = 0
        y_count = 0
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if s1[i] == 'x':
                    x_count += 1
                else:
                    y_count += 1
        if (x_count + y_count) % 2 == 1:
            return -1
        else:
            if x_count % 2 == 0:
                return (x_count + y_count) // 2
            else:
                return (x_count + y_count) // 2 + 1


if __name__ == "__main__":
    # s1 = "xx"
    # s2 = "xy"
    s1 = "xxyyxyxyxx"
    s2 = "xyyxyxxxyx"
    # s1 = "yx"
    # s2 = "xy"
    print(Solution().minimumSwap(s1, s2))
