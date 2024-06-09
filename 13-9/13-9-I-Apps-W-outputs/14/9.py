
def get_brain_latency(n, m, connectors):
    # Initialize a graph with n nodes and m edges
    graph = [[] for _ in range(n)]
    for a, b in connectors:
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)
    
    # Find the maximum distance between any two nodes
    max_distance = 0
    for i in range(n):
        for j in range(i + 1, n):
            distance = bfs(graph, i, j)
            max_distance = max(max_distance, distance)
    
    return max_distance

def bfs(graph, start, end):
    # Breadth-first search
    queue = [start]
    visited = set([start])
    distance = 0
    while queue:
        node = queue.pop(0)
        if node == end:
            return distance
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
        distance += 1
    return distance

n, m = map(int, input().split())
connectors = []
for _ in range(m):
    a, b = map(int, input().split())
    connectors.append((a, b))
print(get_brain_latency(n, m, connectors))

