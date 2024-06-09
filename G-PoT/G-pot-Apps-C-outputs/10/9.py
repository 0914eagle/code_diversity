
# Read input
N, M, alpha = map(int, input().split())
roads = []
for _ in range(M):
    u, v, c = map(int, input().split())
    roads.append((u, v, c))

# Sort roads by the number of candies in descending order
roads.sort(key=lambda x: x[2], reverse=True)

# Initialize variables
min_energy = float('inf')

# Iterate through each road as a starting point
for start in range(M):
    total_candies = 0
    max_candies = 0
    energy = 0
    visited = set()
    current = start

    # Traverse the roads
    while current not in visited:
        visited.add(current)
        u, v, c = roads[current]
        total_candies += c
        max_candies = max(max_candies, c)
        energy = max(energy, max_candies**2 + alpha * len(visited))
        current = (current + 1) % M

    # Check if all roads were visited and update min_energy
    if len(visited) == M:
        min_energy = min(min_energy, energy)

# Output the result
if min_energy == float('inf'):
    print("Poor girl")
else:
    print(min_energy)
