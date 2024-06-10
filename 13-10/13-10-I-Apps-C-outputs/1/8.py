
import sys
input = sys.stdin.read()
input = input.split('\n')

N, M = map(int, input[0].split())
roads = [list(map(int, input[i].split())) for i in range(1, M+1)]

# Find all shortest paths between cities
shortest_paths = {}
for i in range(N):
    shortest_paths[i] = []
    for road in roads:
        if road[0] == i:
            shortest_paths[i].append(road)

# Count the number of shortest paths containing each road
output = []
for road in roads:
    count = 0
    for i in range(N):
        if road[1] == i:
            count += len(shortest_paths[i])
    output.append(count)

# Print the output
for i in output:
    print(i)

