
import sys

def get_brain_latency(n, m, connectors):
    graph = [[] for _ in range(n + 1)]
    for a, b in connectors:
        graph[a].append(b)
        graph[b].append(a)
    
    distances = [float('inf') for _ in range(n + 1)]
    distances[1] = 0
    queue = [1]
    
    while queue:
        vertex = queue.pop(0)
        for neighbor in graph[vertex]:
            if distances[neighbor] == float('inf'):
                distances[neighbor] = distances[vertex] + 1
                queue.append(neighbor)
    
    return max(distances[2:])

n, m = map(int, input().split())
connectors = []
for _ in range(m):
    a, b = map(int, input().split())
    connectors.append((a, b))

print(get_brain_latency(n, m, connectors))

