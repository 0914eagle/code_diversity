
import sys
import math

def get_neighbors(n, m, edges):
    neighbors = [[] for _ in range(n)]
    for u, v in edges:
        neighbors[u].append(v)
        neighbors[v].append(u)
    return neighbors

def bfs(n, m, edges, s, t):
    queue = [(s, 0)]
    visited = set()
    while queue:
        u, dist = queue.pop(0)
        if u == t:
            return dist
        if u in visited:
            continue
        visited.add(u)
        for v in neighbors[u]:
            queue.append((v, dist+1))
    return -1

def solve(n, m, edges, s, t):
    neighbors = get_neighbors(n, m, edges)
    dist = bfs(n, m, edges, s, t)
    if dist == -1:
        return "never meet"
    return dist

if __name__ == '__main__':
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    s, t = map(int, input().split())
    print(solve(n, m, edges, s, t))

