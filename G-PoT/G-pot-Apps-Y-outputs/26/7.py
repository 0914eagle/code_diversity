
from collections import deque

n, m = map(int, input().split())
adj_list = {i: [] for i in range(1, n+1)}
for _ in range(m):
    u, v = map(int, input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

def bfs(start):
    visited = [False] * (n+1)
    dist = [-1] * (n+1)
    queue = deque()
    queue.append(start)
    visited[start] = True
    dist[start] = 0
    while queue:
        node = queue.popleft()
        for neighbor in adj_list[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)
    return dist.index(max(dist))

farthest_node = bfs(1)
farthest_node = bfs(farthest_node)

print(farthest_node)
if m < n - 1:
    for i in range(1, n+1):
        if i != farthest_node:
            print(i, farthest_node)
