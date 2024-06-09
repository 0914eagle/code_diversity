
import sys
input = sys.stdin.read().splitlines()

n, m, k = map(int, input[0].split())
roads = [tuple(map(int, input[i].split())) for i in range(1, m+1)]
routes = [tuple(map(int, input[i].split())) for i in range(m+1, m+1+k)]

# create a graph with the roads as edges
graph = [[] for _ in range(n+1)]
for x, y, w in roads:
    graph[x].append((y, w))
    graph[y].append((x, w))

# find the shortest path between each pair of districts
distances = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]
for i in range(n+1):
    distances[i][i] = 0
    for j, w in graph[i]:
        distances[i][j] = w
        distances[j][i] = w
for k in range(n+1):
    for i in range(n+1):
        for j in range(n+1):
            distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])

# find the minimum total cost of travel for each route
total_cost = 0
for a, b in routes:
    total_cost += distances[a][b]

print(total_cost)

