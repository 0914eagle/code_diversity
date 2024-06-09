
from collections import deque

n, m = map(int, input().split())
adj_list = [[] for _ in range(n+1)]
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
    last_node = start

    while queue:
        node = queue.popleft()
        last_node = node
        for neighbor in adj_list[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                dist[neighbor] = dist[node] + 1
                queue.append(neighbor)

    return last_node, dist[last_node]

farthest_node, _ = bfs(1)
_, diameter = bfs(farthest_node)

print(diameter)

if m < n - 1:
    for i in range(1, n+1):
        if not adj_list[i]:
            print(farthest_node, i)
            break
