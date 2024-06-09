
def min_extra_roads(n, m, s, roads):
    graph = {i: [] for i in range(1, n+1)}
    for u, v in roads:
        graph[u].append(v)

    visited = [False] * (n+1)
    visited[s] = True

    def dfs(node):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)

    dfs(s)

    extra_roads = 0
    for i in range(1, n+1):
        if not visited[i]:
            extra_roads += 1

    return extra_roads

# Reading input
n, m, s = map(int, input().split())
roads = [tuple(map(int, input().split())) for _ in range(m)]

result = min_extra_roads(n, m, s, roads)
print(result)
