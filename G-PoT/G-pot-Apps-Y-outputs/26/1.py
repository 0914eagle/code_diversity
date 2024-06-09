
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
    v, u = map(int, input().split())
    graph[v-1].append(u-1)
    graph[u-1].append(v-1)

if m == n - 1:
    _, diameter = bfs(graph, 0)
    print(diameter)
else:
    endpoints, _ = bfs(graph, 0)
    _, diameter = bfs(graph, endpoints)
    print(diameter)
    
    for i in range(n):
        if i != endpoints:
            print(endpoints + 1, i + 1)
