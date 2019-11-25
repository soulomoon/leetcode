from collections import Counter
from typing import List


class Solution:
    def isNStraightHand_ac(self, hand: List[int], W: int) -> bool:
        if len(hand) % W != 0:
            return False
        g_number = len(hand) // W
        c = Counter(hand)
        for _ in range(g_number):
            e = None
            for _ in range(W):
                if e is None:
                    e = min(c.keys())
                else:
                    e += 1

                if e not in c:
                    return False
                else:
                    c[e] -= 1
                    if c[e] == 0:
                        del c[e]
        return True

    def isNStraightHand_slow(self, hand: List[int], W: int) -> bool:
        if len(hand) % W != 0:
            return False
        g_number = len(hand) // W

        def append(group, element):
            if len(group) < W and (not group or group[-1] + 1 == element):
                group.append(element)
                return True
            else:
                return False

        gs = [[] for _ in range(g_number)]
        hand.sort()
        for e in hand:
            for g in gs:
                if append(g, e):
                    break
            else:
                return False
        return True


if __name__ == "__main__":
    # hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
    # W = 3
    hand = [0, 0]
    W = 2
    print(Solution().isNStraightHand(hand, W))
