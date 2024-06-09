
# Read input
N, M, alpha = map(int, input().split())
roads = []
for _ in range(M):
    u, v, c = map(int, input().split())
    roads.append((u, v, c))

# Sort roads by the number of candies in ascending order
roads.sort(key=lambda x: x[2])

# Initialize variables
min_energy = float('inf')

# Iterate through each road as the starting point
for start_road in roads:
    u, v, candies = start_road
    energy = candies ** 2 + alpha
    visited = set([start_road])

    # Traverse through other roads without visiting the same road twice
    current_junction = v
    while len(visited) < N:
        next_road = None
        for road in roads:
            if road not in visited and (road[0] == current_junction or road[1] == current_junction):
                next_road = road
                break
        if next_road is None:
            break
        visited.add(next_road)
        energy += next_road[2] ** 2 + alpha
        current_junction = next_road[1] if next_road[0] == current_junction else next_road[0]

    # Check if all junctions are visited and update minimum energy
    if len(visited) == N and current_junction == v:
        min_energy = min(min_energy, energy)

# Output the result
if min_energy == float('inf'):
    print("Poor girl")
else:
    print(min_energy)
