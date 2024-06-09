
def solve(n, m, k, roads, routes):
    # Initialize a graph with the given roads
    graph = {i: set() for i in range(1, n + 1)}
    for x, y, w in roads:
        graph[x].add((y, w))
        graph[y].add((x, w))

    # Initialize the distance array with the given routes
    distances = [float("inf") for _ in range(k)]
    for i, (a, b) in enumerate(routes):
        distances[i] = graph[a][b][1]

    # Find the minimum total cost by making at most one road cost zero
    min_cost = float("inf")
    for i in range(m):
        x, y, w = roads[i]
        new_graph = graph.copy()
        new_graph[x] = set()
        new_graph[y] = set()
        new_distances = [float("inf") for _ in range(k)]
        for j, (a, b) in enumerate(routes):
            if a == x and b == y:
                new_distances[j] = 0
            elif a == y and b == x:
                new_distances[j] = w
            else:
                new_distances[j] = graph[a][b][1]
        min_cost = min(min_cost, sum(new_distances))

    return min_cost

