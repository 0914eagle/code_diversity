
from collections import defaultdict

def dfs(graph, visited, node):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, visited, neighbor)

n, m, s = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

visited = [False] * (n + 1)
dfs(graph, visited, s)

extra_roads = 0
for i in range(1, n + 1):
    if not visited[i]:
        extra_roads += 1

print(extra_roads)
