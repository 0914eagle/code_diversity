
import sys

def find_minimum_energy(N, M, alpha, roads):
    graph = {}
    for u, v, c in roads:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append((v, c))
        graph[v].append((u, c))

    def dfs(node, start_node, visited, candies):
        if node == start_node and len(visited) == M:
            return max(candies) ** 2 + alpha * len(visited)
        
        min_energy = float('inf')
        for neighbor, candy in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                min_energy = min(min_energy, dfs(neighbor, start_node, visited, candies + [candy]))
                visited.remove(neighbor)
        
        return min_energy

    min_energy = float('inf')
    for node in range(1, N+1):
        visited = set([node])
        min_energy = min(min_energy, dfs(node, node, visited, []))
    
    return min_energy if min_energy != float('inf') else "Poor girl"

# Read input
N, M, alpha = map(int, input().split())
roads = [tuple(map(int, input().split())) for _ in range(M)]

# Find and print the minimum energy
print(find_minimum_energy(N, M, alpha, roads))
