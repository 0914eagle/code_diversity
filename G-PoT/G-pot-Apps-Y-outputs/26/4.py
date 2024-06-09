
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
    return max(distance), distance.index(max(distance))

def find_diameter():
    _, farthest_node = bfs(1)
    diameter, _ = bfs(farthest_node)
    return diameter

diameter = find_diameter()
print(diameter)

if m < n - 1:
    remaining_edges = n - 1 - m
    for i in range(1, n):
        for j in range(i+1, n+1):
            if remaining_edges == 0:
                break
            if j not in adj_list[i]:
                print(i, j)
                remaining_edges -= 1
