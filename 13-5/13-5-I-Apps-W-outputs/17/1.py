
def f1(n, m, k, roads, storages):
    # Initialize the graph with the given roads
    graph = [[] for _ in range(n + 1)]
    for u, v, l in roads:
        graph[u].append((v, l))
        graph[v].append((u, l))
    
    # Initialize the distances from each city to each storage
    distances = [[float('inf')] * k for _ in range(n + 1)]
    for i in range(k):
        distances[storages[i]][i] = 0
    
    # Relax the distances iteratively
    for _ in range(n):
        for u in range(1, n + 1):
            for v, l in graph[u]:
                for i in range(k):
                    distances[u][i] = min(distances[u][i], distances[v][i] + l)
    
    # Find the minimum distance from each city to a storage
    min_distances = [float('inf')] * n
    for i in range(k):
        for u in range(1, n + 1):
            min_distances[u - 1] = min(min_distances[u - 1], distances[u][i])
    
    return min_distances

def f2(n, m, k, roads, storages):
    # Initialize the graph with the given roads
    graph = [[] for _ in range(n + 1)]
    for u, v, l in roads:
        graph[u].append((v, l))
        graph[v].append((u, l))
    
    # Initialize the distances from each city to each storage
    distances = [[float('inf')] * k for _ in range(n + 1)]
    for i in range(k):
        distances[storages[i]][i] = 0
    
    # Relax the distances iteratively
    for _ in range(n):
        for u in range(1, n + 1):
            for v, l in graph[u]:
                for i in range(k):
                    distances[u][i] = min(distances[u][i], distances[v][i] + l)
    
    # Find the minimum distance from each city to a storage
    min_distances = [float('inf')] * n
    for i in range(k):
        for u in range(1, n + 1):
            min_distances[u - 1] = min(min_distances[u - 1], distances[u][i])
    
    # Find the city with the minimum distance to a storage
    min_city = min(range(n), key=lambda i: min_distances[i])
    
    # Find the storage with the minimum distance from the minimum city
    min_storage = min(range(k), key=lambda i: distances[min_city + 1][i])
    
    return min_city + 1, min_storage + 1

if __name__ == '__main__':
    n, m, k = map(int, input().split())
    roads = [list(map(int, input().split())) for _ in range(m)]
    storages = list(map(int, input().split())) if k > 0 else []
    print(*f2(n, m, k, roads, storages))

