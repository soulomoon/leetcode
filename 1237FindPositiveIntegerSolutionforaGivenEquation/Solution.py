"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):

"""
import functools
from typing import List, Set, Tuple


class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        return [list(t) for t in findSolution_rec(customfunction, z, 1, 1)]


@functools.lru_cache
def findSolution_rec(customfunction: 'CustomFunction', z: int, x: int, y: int) -> Set[Tuple[int, int]]:
    r = customfunction.f(x, y)
    if r > z:
        return set()
    elif r == z:
        return {(x, y)}
    else:
        return findSolution_rec(customfunction, z, x + 1, y).union(findSolution_rec(customfunction, z, x, y + 1))
