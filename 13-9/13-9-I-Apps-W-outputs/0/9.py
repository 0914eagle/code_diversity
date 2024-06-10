
def dfs(node, visited, neighbors, times):
    visited[node] = True
    for neighbor in neighbors[node]:
        if not visited[neighbor]:
            dfs(neighbor, visited, neighbors, times)
    times[node] = min(times[node], min(times[neighbor] for neighbor in neighbors[node]))

def solve(n, k, times):
    neighbors = {i: [] for i in range(1, n + 1)}
    for i in range(1, n):
        u, v = map(int, input().split())
        neighbors[u].append(v)
        neighbors[v].append(u)
    visited = [False] * (n + 1)
    dfs(1, visited, neighbors, times)
    return times[1]

if __name__ == '__main__':
    n, k = map(int, input().split())
    times = list(map(int, input().split()))
    print(solve(n, k, times))

