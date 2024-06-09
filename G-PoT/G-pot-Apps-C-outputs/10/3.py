
import sys

def find_min_energy(N, M, alpha, roads):
    adj_list = [[] for _ in range(N)]
    for u, v, c in roads:
        adj_list[u-1].append((v-1, c))
        adj_list[v-1].append((u-1, c))

    def dfs(node, start, candies, visited):
        visited[node] = True
        if node == start and len(candies) == M:
            return max(candies)**2 + alpha*len(candies)
        
        min_energy = float('inf')
        for neighbor, candy in adj_list[node]:
            if not visited[neighbor]:
                min_energy = min(min_energy, dfs(neighbor, start, candies + [candy], visited[:]))
        
        return min_energy

    min_energy = float('inf')
    for i in range(N):
        min_energy = min(min_energy, dfs(i, i, [], [False]*N))

    return min_energy if min_energy != float('inf') else "Poor girl"

# Read input
N, M, alpha = map(int, input().split())
roads = [list(map(int, input().split())) for _ in range(M)]

# Find and print the minimum amount of energy
print(find_min_energy(N, M, alpha, roads))
