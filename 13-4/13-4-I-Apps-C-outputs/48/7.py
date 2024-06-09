
import sys

def f1(N, edges):
    # Initialize the graph with N vertices and no edges
    graph = [[] for _ in range(N)]

    # Add edges to the graph
    for edge in edges:
        graph[edge[0] - 1].append(edge[1] - 1)
        graph[edge[1] - 1].append(edge[0] - 1)

    # Find the shortest path between each pair of vertices
    dist = [[float('inf') for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j:
                dist[i][j] = find_shortest_path(graph, i, j)

    # Count the number of pairs that satisfy the condition
    count = 0
    for i in range(N):
        for j in range(i + 1, N):
            if dist[i][j] != float('inf'):
                count += 1

    return count % (10**9 + 7)

def find_shortest_path(graph, start, end):
    queue = [(start, 0)]
    visited = set()

    while queue:
        node, dist = queue.pop(0)
        if node == end:
            return dist
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                queue.append((neighbor, dist + 1))

    return float('inf')

def f2(N, edges):
    # Initialize the graph with N vertices and no edges
    graph = [[] for _ in range(N)]

    # Add edges to the graph
    for edge in edges:
        graph[edge[0] - 1].append(edge[1] - 1)
        graph[edge[1] - 1].append(edge[0] - 1)

    # Find the shortest path between each pair of vertices
    dist = [[float('inf') for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i != j:
                dist[i][j] = find_shortest_path(graph, i, j)

    # Count the number of pairs that satisfy the condition
    count = 0
    for i in range(N):
        for j in range(i + 1, N):
            if dist[i][j] != float('inf'):
                count += 1

    return count % (10**9 + 7)

if __name__ == '__main__':
    N = int(input())
    edges = []
    for _ in range(N - 1):
        edges.append(list(map(int, input().split())))
    print(f2(N, edges))

