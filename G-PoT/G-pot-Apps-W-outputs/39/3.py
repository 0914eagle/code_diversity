
import itertools

def floyd_warshall(graph, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

def find_longest_shortest_path(graph, n):
    floyd_warshall(graph, n)
    max_length = 0
    for i, j in itertools.combinations(range(n), 2):
        max_length = max(max_length, graph[i][j])
    return max_length

# Read input
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# Find and output the result
result = find_longest_shortest_path(graph, n)
print(result)
