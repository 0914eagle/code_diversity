
import itertools

def floyd_warshall(graph, n):
    for k, i, j in itertools.permutations(range(n), 3):
        graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    max_shortest_path = max([max(row) for row in graph])
    return max_shortest_path

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

result = floyd_warshall(graph, N)
print(result)
