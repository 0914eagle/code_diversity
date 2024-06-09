
import sys

def find_min_energy(N, M, alpha, roads):
    adj_list = {i: [] for i in range(1, N+1)}
    for u, v, c in roads:
        adj_list[u].append((v, c))
        adj_list[v].append((u, c))

    min_energy = float('inf')

    for start_node in range(1, N+1):
        visited = set()
        current_node = start_node
        total_candies = 0
        max_candies = 0
        num_roads = 0

        while current_node not in visited:
            visited.add(current_node)
            max_candies = max(max_candies, max(c for _, c in adj_list[current_node]))
            total_candies += sum(c for _, c in adj_list[current_node])
            num_roads += 1

            next_node = max((v, c) for v, c in adj_list[current_node] if v not in visited)[0]
            current_node = next_node

        if len(visited) == N and num_roads == M:
            energy = max_candies ** 2 + alpha * num_roads
            min_energy = min(min_energy, energy)

    return min_energy if min_energy != float('inf') else "Poor girl"

# Read input
N, M, alpha = map(int, input().split())
roads = [list(map(int, input().split())) for _ in range(M)]

# Find and print the minimum energy
print(find_min_energy(N, M, alpha, roads))
