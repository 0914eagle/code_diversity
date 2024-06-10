ulate_rebuilds(n, m, roads, k, path):
    graph = {i: [] for i in range(1, n + 1)}
    for u, v in roads:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = set()
    rebuilds_min = 0
    rebuilds_max = 0
    
    for i in range(1, k - 1):
        visited.add(path[i])
        if path[i + 1] not in graph[path[i]]:
            rebuilds_min += 1
    
    for i in range(1, k):
        for neighbor in graph[path[i]]:
            if neighbor not in visited:
                rebuilds_max += 1
    
    return rebuilds_min, rebuilds_max

if __name__ == "__main__":
    n, m = map(int, input().split())
    roads = [tuple(map(int, input().split())) for _ in range(m)]
    k = int(input())
    path = list(map(int, input().split()))
    
    min_rebuilds, max_rebuilds = calculate_rebuilds(n, m, roads, k, path)
    print(min_rebuilds, max_rebuilds)
