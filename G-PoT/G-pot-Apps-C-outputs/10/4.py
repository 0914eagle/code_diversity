
# Read input values
N, M, alpha = map(int, input().split())
roads = []
for _ in range(M):
    u, v, c = map(int, input().split())
    roads.append((u, v, c))

# Sort roads by the number of candies in ascending order
roads.sort(key=lambda x: x[2])

# Initialize variables
min_energy = float('inf')

# Iterate through each road as a starting point
for start in range(M):
    total_candies = 0
    max_candies = 0
    energy = 0
    visited = set()
    current = start

    # Traverse the roads without visiting the same road twice
    while len(visited) < M:
        u, v, c = roads[current]
        total_candies += c
        max_candies = max(max_candies, c)
        visited.add(current)
        current = (current + 1) % M

        # Check if all roads have been visited
        if len(visited) == M:
            energy = max_candies ** 2 + alpha * len(visited)
            min_energy = min(min_energy, energy)

    # Check if the total number of candies is equal to the sum of all candies
    if total_candies == sum(c for _, _, c in roads):
        break

if min_energy == float('inf'):
    print("Poor girl")
else:
    print(min_energy)
