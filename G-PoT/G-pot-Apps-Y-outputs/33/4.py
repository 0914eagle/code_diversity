
from collections import defaultdict

def dfs(graph, node, visited):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited)

n, m, s = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

visited = [False] * (n + 1)
dfs(graph, s, visited)

reachable_count = sum(visited) - 1

print(n - reachable_count)
