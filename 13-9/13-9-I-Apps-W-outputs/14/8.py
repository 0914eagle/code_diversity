
import sys
input = sys.stdin.read()
n, m = map(int, input.split())

# Initialize a graph with n nodes and 0 edges
graph = [[] for i in range(n + 1)]

# Add edges to the graph
for i in range(m):
    a, b = map(int, input.split())
    graph[a].append(b)
    graph[b].append(a)

# Find the maximum distance between any two nodes
max_distance = 0
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        distance = bfs(graph, i, j)
        if distance > max_distance:
            max_distance = distance

print(max_distance)

# Breadth-first search function to find the shortest path between two nodes
def bfs(graph, start, end):
    queue = [start]
    visited = set()
    while queue:
        node = queue.pop(0)
        if node == end:
            return len(visited) - 1
        if node not in visited:
            visited.add(node)
            queue += graph[node]
    return 0

