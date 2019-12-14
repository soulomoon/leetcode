from collections import defaultdict
from math import inf
from typing import List


class Graph:

    def __init__(self, n, edges):
        self.parent = [-1] * n
        self.low = [inf] * n
        self.disc = [inf] * n
        self.visited = [False] * n
        self.graph: List = [[] for i in range(n)]
        self.Time = 0
        self.result = []
        for u, v in edges:
            self.add_edge(u, v)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bridge_util(self, u):
        self.visited[u] = True
        self.disc[u] = self.Time
        self.low[u] = self.Time
        self.Time += 1
        for v in self.graph[u]:
            if not self.visited[v]:
                self.parent[v] = u
                self.bridge_util(v)
                self.low[u] = min(self.low[u], self.low[v])
                if self.low[v] > self.disc[u]:
                    self.result.append((u, v))
            elif v != self.parent[u]:
                self.low[u] = min(self.low[u], self.disc[v])

    def bridge(self):
        self.bridge_util(0)
