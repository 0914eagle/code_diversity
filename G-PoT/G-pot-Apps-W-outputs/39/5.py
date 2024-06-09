
import itertools

def floyd_warshall(graph):
    n = len(graph)
    dist = [row[:] for row in graph]
    for k, i, j in itertools.permutations(range(n), 3):
        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return max(max(row) for row in dist)

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
result = floyd_warshall(graph)
print(result)
