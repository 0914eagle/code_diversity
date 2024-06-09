
from collections import deque

n, m = map(int, input().split())
adj_list = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    adj_list[u].append(v)
    adj_list[v].append(u)

def bfs(start):
    visited = [False] * (n+1)
    distance = [0] * (n+1)
    queue = deque()
    queue.append(start)
    visited[start] = True
    max_distance = 0
    max_node = start

    while queue:
        node = queue.popleft()
        for neighbor in adj_list[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                distance[neighbor] = distance[node] + 1
                if distance[neighbor] > max_distance:
                    max_distance = distance[neighbor]
                    max_node = neighbor
                queue.append(neighbor)

    return max_node, max_distance

farthest_node, _ = bfs(1)
_, diameter = bfs(farthest_node)

print(diameter)

if m < n - 1:
    for i in range(1, n+1):
        if i != farthest_node:
            print(f"{farthest_node} {i}")
