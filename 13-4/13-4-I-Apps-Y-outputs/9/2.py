
import sys
input = sys.stdin.read().splitlines()

n, m, k = map(int, input[0].split())
roads = [tuple(map(int, input[i].split())) for i in range(1, m+1)]
routes = [tuple(map(int, input[i].split())) for i in range(m+1, m+1+k)]

# create a dictionary to store the cost of travel between each pair of districts
d = {}
for road in roads:
    x, y, w = road
    if x not in d:
        d[x] = {}
    if y not in d:
        d[y] = {}
    d[x][y] = w
    d[y][x] = w

# find the minimum cost of travel between each pair of districts
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            d[i][j] = 0
        elif d[i][j] > d[i][k] + d[k][j]:
            d[i][j] = d[i][k] + d[k][j]

# find the minimum total cost of travel for each route
total_cost = 0
for route in routes:
    x, y = route
    total_cost += d[x][y]

print(total_cost)

