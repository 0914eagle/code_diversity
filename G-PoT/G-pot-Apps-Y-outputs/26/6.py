
from collections import deque

n, m = map(int, input().split())
adj_list = {i: [] for i in range(1, n+1)}
for _ in range(m):
    u, v = map(int, input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

def bfs(start):
    visited = [False] * (n+1)
    distance = [0] * (n+1)
    queue = deque([start])
    visited[start] = True
    while queue:
        node = queue.popleft()
        for neighbor in adj_list[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                distance[neighbor] = distance[node] + 1
                queue.append(neighbor)
    return distance.index(max(distance))

farthest_node = bfs(1)
farthest_node = bfs(farthest_node)

print(farthest_node)
if m < n - 1:
    for i in range(1, n+1):
        if i != farthest_node:
            print(farthest_node, i)
