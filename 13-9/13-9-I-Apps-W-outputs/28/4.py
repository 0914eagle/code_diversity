
import sys

class Graph:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.adj_list = [[] for _ in range(n + 1)]

    def add_edge(self, u, v):
        self.adj_list[u].append(v)

    def dfs(self, src, visited):
        visited[src] = True
        for neighbor in self.adj_list[src]:
            if not visited[neighbor]:
                self.dfs(neighbor, visited)

    def is_cyclic(self):
        visited = [False] * (self.n + 1)
        for node in range(1, self.n + 1):
            if not visited[node]:
                self.dfs(node, visited)
        return visited[0]

def solve():
    n, m = map(int, input().split())
    graph = Graph(n, m)
    for i in range(m):
        u, v = map(int, input().split())
        graph.add_edge(u, v)
    if graph.is_cyclic():
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    solve()

