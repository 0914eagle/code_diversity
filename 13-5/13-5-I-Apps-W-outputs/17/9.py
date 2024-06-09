
def find_min_cost(n, m, k, roads, storages):
    # Initialize graph with costs
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    for u, v, l in roads:
        graph[u][v] = l
        graph[v][u] = l

    # Initialize distances from each city to each other city
    distances = [[float("inf") for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        distances[i][i] = 0

    # Floyd-Warshall algorithm to find shortest paths between all pairs of cities
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                distances[i][j] = min(distances[i][j], distances[i][k] + distances[k][j])

    # Initialize minimum cost to open bakery and choose storage and path
    min_cost = float("inf")

    # Iterate over all possible cities to open bakery
    for b in range(1, n + 1):
        # If the city has no storage, skip it
        if b not in storages:
            continue
        # Initialize minimum cost to open bakery and choose storage and path in this city
        min_cost_in_city = float("inf")
        # Iterate over all possible storages in this city
        for s in range(1, n + 1):
            # If the storage is not in this city, skip it
            if s not in storages or s == b:
                continue
            # Initialize minimum cost to open bakery and choose this storage and path
            min_cost_with_storage = float("inf")
            # Iterate over all possible paths between bakery and storage
            for path in all_paths(graph, b, s):
                # Calculate cost of this path
                cost = sum(graph[u][v] for u, v in zip(path, path[1:]))
                # If the cost is less than the current minimum cost, update the minimum cost
                if cost < min_cost_with_storage:
                    min_cost_with_storage = cost
            # If the minimum cost with this storage is less than the current minimum cost in this city, update the minimum cost in this city
            if min_cost_with_storage < min_cost_in_city:
                min_cost_in_city = min_cost_with_storage
        # If the minimum cost in this city is less than the current minimum cost, update the minimum cost
        if min_cost_in_city < min_cost:
            min_cost = min_cost_in_city

    return min_cost if min_cost != float("inf") else -1

def all_paths(graph, start, end):
    paths = []
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for neighbor in range(1, len(graph)):
            if graph[vertex][neighbor] > 0 and neighbor not in path:
                new_path = path + [neighbor]
                if neighbor == end:
                    paths.append(new_path)
                else:
                    queue.append((neighbor, new_path))
    return paths

if __name__ == '__main__':
    n, m, k = map(int, input().split())
    roads = [list(map(int, input().split())) for _ in range(m)]
    storages = list(map(int, input().split())) if k > 0 else []
    print(find_min_cost(n, m, k, roads, storages))

