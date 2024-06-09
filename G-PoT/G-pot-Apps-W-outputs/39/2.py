
import itertools

def floyd_warshall(graph, n):
    for k, i, j in itertools.permutations(range(n), 3):
        graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    longest_shortest_path = max([max(row) for row in graph])
    return longest_shortest_path

# Read input
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

result = floyd_warshall(graph, n)
print(result)
