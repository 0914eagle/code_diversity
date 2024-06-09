
def get_brain_latency(n, m, brain_connectors):
    # Initialize a graph with n vertices
    graph = [[] for _ in range(n)]

    # Add edges to the graph
    for a, b in brain_connectors:
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)

    # Find the maximum distance between any two vertices
    max_distance = 0
    for i in range(n):
        for j in range(n):
            if i != j:
                distance = bfs(graph, i, j)
                max_distance = max(max_distance, distance)

    return max_distance

def bfs(graph, start, end):
    # Breadth-first search
    queue = [start]
    visited = set()
    distance = 0
    while queue:
        vertex = queue.pop(0)
        if vertex == end:
            return distance
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
        distance += 1
    return -1

n, m = map(int, input().split())
brain_connectors = []
for _ in range(m):
    a, b = map(int, input().split())
    brain_connectors.append((a, b))
print(get_brain_latency(n, m, brain_connectors))

