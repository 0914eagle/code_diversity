
def get_min_cost(n, m, k, roads, storages):
    # Initialize graph with distances between cities
    graph = {}
    for i in range(n):
        graph[i] = {}
    for u, v, l in roads:
        graph[u][v] = l
        graph[v][u] = l

    # Initialize distances from each city to the storage cities
    dist_to_storage = [float('inf')] * n
    for i in range(k):
        dist_to_storage[storages[i] - 1] = 0

    # Floyd-Warshall algorithm to find shortest distances between all pairs of cities
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    # Find the city with the minimum cost to reach a storage city
    min_cost = float('inf')
    for i in range(n):
        for j in range(k):
            min_cost = min(min_cost, graph[i][storages[j] - 1] + dist_to_storage[storages[j] - 1])

    return min_cost

def main():
    n, m, k = map(int, input().split())
    roads = []
    for _ in range(m):
        u, v, l = map(int, input().split())
        roads.append((u, v, l))
    storages = list(map(int, input().split()))
    print(get_min_cost(n, m, k, roads, storages))

if __name__ == '__main__':
    main()

