
from collections import deque

def bfs(graph, start):
    visited = [False] * len(graph)
    distance = [0] * len(graph)
    
    queue = deque()
    queue.append(start)
    visited[start] = True
    
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                distance[neighbor] = distance[node] + 1
                queue.append(neighbor)
    
    max_distance_node = distance.index(max(distance))
    return max_distance_node, max(distance)

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

diameter = 0
if m == n - 1:
    _, diameter = bfs(graph, 0)
else:
    leaf_node, _ = bfs(graph, 0)
    _, diameter = bfs(graph, leaf_node)

print(diameter)

if m < n - 1:
    for i in range(1, n):
        if len(graph[i]) == 1:
            print(i+1, 1)
            break
