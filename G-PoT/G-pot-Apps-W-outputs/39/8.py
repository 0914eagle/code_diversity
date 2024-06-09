
import itertools

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

max_shortest_path = 0

for i, j in itertools.combinations(range(N), 2):
    shortest_path = graph[i][j]
    for k in range(N):
        if k != i and k != j:
            shortest_path = min(shortest_path, graph[i][k] + graph[k][j])
    max_shortest_path = max(max_shortest_path, shortest_path)

print(max_shortest_path)
