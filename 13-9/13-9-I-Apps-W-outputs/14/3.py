
import sys
input = sys.stdin.read()
n, m = map(int, input.split())

# Initialize the brain connectors and their distances
brain_connectors = []
distances = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            distances[i][j] = 0
        else:
            distances[i][j] = float('inf')

# Read the brain connectors and their distances
for i in range(m):
    a, b = map(int, input.split())
    brain_connectors.append((a, b))
    distances[a][b] = 1

# Floyd-Warshall algorithm to find the shortest distances between all pairs of brains
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if distances[i][k] + distances[k][j] < distances[i][j]:
                distances[i][j] = distances[i][k] + distances[k][j]

# Find the maximum distance between any two brains
max_distance = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if distances[i][j] > max_distance:
            max_distance = distances[i][j]

print(max_distance)

