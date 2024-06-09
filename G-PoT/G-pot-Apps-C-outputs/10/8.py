
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

# Iterate through each road to find the minimum energy
for i in range(M):
    u, v, c = roads[i]
    energy = c**2 + alpha * (i + 1)
    if energy < min_energy:
        min_energy = energy

# Output the result
if min_energy == float('inf'):
    print("Poor girl")
else:
    print(min_energy)
