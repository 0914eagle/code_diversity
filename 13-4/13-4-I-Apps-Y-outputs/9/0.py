
def solve(n, m, k, roads, courier_routes):
    # Initialize a graph with the given roads
    graph = {i: set() for i in range(1, n + 1)}
    for x, y, w in roads:
        graph[x].add((y, w))
        graph[y].add((x, w))

    # Initialize the distance matrix with the given courier routes
    distance = [[float("inf") for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        distance[i][i] = 0
    for a, b in courier_routes:
        distance[a][b] = 1

    # Floyd-Warshall algorithm to find the shortest path between all pairs of districts
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

    # Find the minimum total courier routes cost by making at most one road cost zero
    min_cost = float("inf")
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j and distance[i][j] != float("inf"):
                min_cost = min(min_cost, distance[i][j])
    return min_cost

