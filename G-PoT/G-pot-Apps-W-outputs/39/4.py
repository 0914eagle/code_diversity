
import itertools

def floyd_warshall(graph):
    n = len(graph)
    dist = [row[:] for row in graph]

    for k, i, j in itertools.product(range(n), repeat=3):
        if dist[i][j] > dist[i][k] + dist[k][j]:
            dist[i][j] = dist[i][k] + dist[k][j]

    return dist

def max_shortest_path(graph):
    dist = floyd_warshall(graph)
    max_length = max(max(row) for row in dist)
    return max_length

# Read input
N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

# Calculate and output result
result = max_shortest_path(graph)
print(result)
