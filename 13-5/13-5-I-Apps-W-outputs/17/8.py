
def f1(n, m, k, roads, storages):
    # Initialize graph with distances between cities
    graph = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]
    for i in range(n+1):
        graph[i][i] = 0
    for u, v, l in roads:
        graph[u][v] = l
        graph[v][u] = l

    # Floyd-Warshall algorithm to find shortest distances between all pairs of cities
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    # Find the minimum cost for each city to have a bakery and a storage
    min_cost = [float('inf') for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j] != float('inf'):
                min_cost[i] = min(min_cost[i], graph[i][j] + storages[j-1])

    # Find the city with the minimum cost
    min_index = min(range(n+1), key=lambda i: min_cost[i])

    return min_cost[min_index]

def f2(n, m, k, roads, storages):
    # Initialize graph with distances between cities
    graph = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]
    for i in range(n+1):
        graph[i][i] = 0
    for u, v, l in roads:
        graph[u][v] = l
        graph[v][u] = l

    # Floyd-Warshall algorithm to find shortest distances between all pairs of cities
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    # Find the minimum cost for each city to have a bakery and a storage
    min_cost = [float('inf') for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j] != float('inf'):
                min_cost[i] = min(min_cost[i], graph[i][j] + storages[j-1])

    # Find the city with the minimum cost
    min_index = min(range(n+1), key=lambda i: min_cost[i])

    return min_index

if __name__ == '__main__':
    n, m, k = map(int, input().split())
    roads = []
    for _ in range(m):
        u, v, l = map(int, input().split())
        roads.append((u, v, l))
    storages = []
    if k > 0:
        storages = list(map(int, input().split()))

    print(f1(n, m, k, roads, storages))
    print(f2(n, m, k, roads, storages))

