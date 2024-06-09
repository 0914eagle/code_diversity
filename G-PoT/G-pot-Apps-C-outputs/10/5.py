
import sys

def find_min_energy(N, M, alpha, roads):
    adj_list = [[] for _ in range(N+1)]
    for u, v, c in roads:
        adj_list[u].append((v, c))
        adj_list[v].append((u, c))

    def dfs(node, start, candies, energy):
        nonlocal min_energy
        if len(candies) == M:
            min_energy = min(min_energy, candies[-1][1]**2 + alpha*len(candies))
            return

        for neighbor, candy in adj_list[node]:
            if (node, neighbor, candy) not in candies and (neighbor, node, candy) not in candies:
                candies.append((node, neighbor, candy))
                dfs(neighbor, start, candies, energy + candy)
                candies.pop()

    min_energy = sys.maxsize
    for i in range(1, N+1):
        dfs(i, i, [], 0)

    return min_energy if min_energy != sys.maxsize else "Poor girl"

# Read input
N, M, alpha = map(int, input().split())
roads = [list(map(int, input().split())) for _ in range(M)]

# Call the function and print the result
result = find_min_energy(N, M, alpha, roads)
print(result)
