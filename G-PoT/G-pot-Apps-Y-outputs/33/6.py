
from collections import defaultdict

def dfs(graph, visited, start):
    stack = [start]
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            stack.extend([neighbor for neighbor in graph[node] if not visited[neighbor]])

n, m, s = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

visited = [False] * (n+1)
dfs(graph, visited, s)

unreachable_cities = sum(1 for i in range(1, n+1) if not visited[i])
print(unreachable_cities - 1 if unreachable_cities > 0 else 0)
