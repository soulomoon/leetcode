from dataclasses import dataclass
from math import inf
from typing import Set, Dict, Optional, Deque
from collections import deque, Counter


class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        res = 0
        if Counter(s1) != Counter(s2):
            return -1
        out_count: Dict[str, Dict[str, int]] = {}
        l = len(s1)
        for i in range(l):
            if s1[i] != s2[i]:
                out_count.setdefault(s1[i], {s2[i]: 0})
                out_count[s1[i]][s2[i]] += 1
        while out_count:
            source = next(iter(out_count.keys()))
            start = next(iter(out_count[source].keys()))
            res += bfs(out_count, source, start)
        return res


@dataclass
class Node:
    char: str
    limit: int  # minimal pipe
    depth: int


# find each chain that route back to source
def bfs(out_count: Dict[str, Dict[str, int]], source, start):
    print(source, start)
    res = 0
    while source in out_count and start in out_count[source]:
        total_limit = out_count[source][start]
        visited: Dict[str, str] = {start: source}
        stack: Deque[Node] = deque()
        stack.append(Node(char=start, limit=total_limit, depth=0))
        current: Optional[Node] = None
        while stack:
            current = stack.popleft()
            for nxt_char in out_count[current.char]:
                if nxt_char not in visited:
                    visited[nxt_char] = current.char
                    next_node = Node(char=nxt_char,
                                     limit=min(out_count[current.char][nxt_char], current.limit),
                                     depth=current.depth + 1)
                    if next_node.char == source:
                        current = next_node
                        break
                    stack.append(next_node)
        # print(current, visited, out_count)
        current_char = current.char
        while visited[current_char] in out_count:
            # print(current_char, visited, out_count)
            out_count[visited[current_char]][current_char] -= current.limit
            # add up
            res += current.limit
            if out_count[visited[current_char]][current_char] == 0:
                del out_count[visited[current_char]][current_char]
                if not out_count[visited[current_char]]:
                    del out_count[visited[current_char]]
            current_char = visited[current_char]
        res -= current.limit
    return res


if __name__ == "__main__":
    # s1 = "xx"
    # s2 = "xy"

    s1 = "yx"
    s2 = "xy"
    print(Solution().minimumSwap(s1, s2))
