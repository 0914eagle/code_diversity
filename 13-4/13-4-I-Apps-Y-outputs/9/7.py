
import sys
input = sys.stdin.read().splitlines()

n, m, k = map(int, input[0].split())
roads = [tuple(map(int, input[i].split())) for i in range(1, m+1)]
routes = [tuple(map(int, input[i].split())) for i in range(m+1, m+1+k)]

# create a graph with roads as edges and weights
graph = {i: {} for i in range(1, n+1)}
for x, y, w in roads:
    graph[x][y] = w
    graph[y][x] = w

# find the shortest path between each pair of districts using Dijkstra's algorithm
from heapq import *
from collections import defaultdict

def dijkstra(graph, start):
    distances = defaultdict(lambda: float('inf'))
    previous = defaultdict(lambda: None)
    queue = [(0, start)]
    while queue:
        dist, node = heappop(queue)
        if distances[node] < dist:
            continue
        for neighbor, weight in graph[node].items():
            distance = dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = node
                heappush(queue, (distance, neighbor))
    return distances, previous

distances, previous = dijkstra(graph, 1)

# find the minimum total courier routes cost
total_cost = 0
for a, b in routes:
    total_cost += distances[b]

print(total_cost)

