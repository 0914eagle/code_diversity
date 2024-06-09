
import itertools

def floyd_warshall(graph):
    n = len(graph)
    dist = [[float('inf') for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            dist[i][j] = graph[i][j]

    for k, i, j in itertools.permutations(range(n), 3):
        dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    max_shortest_path = max([max(row) for row in dist])
    return max_shortest_path

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

result = floyd_warshall(graph)
print(result)