
def solve(n, m, k, roads, routes):
    # Initialize a graph with the given roads
    graph = {i: set() for i in range(1, n + 1)}
    for x, y, w in roads:
        graph[x].add((y, w))
        graph[y].add((x, w))

    # Find the shortest path between each pair of districts using Dijkstra's algorithm
    distances = {i: float("inf") for i in range(1, n + 1)}
    previous = {i: None for i in range(1, n + 1)}
    queue = [(0, 1)]
    while queue:
        dist, node = heapq.heappop(queue)
        if dist > distances[node]:
            continue
        for neighbor, w in graph[node]:
            v = dist + w
            if v < distances[neighbor]:
                distances[neighbor] = v
                previous[neighbor] = node
                heapq.heappush(queue, (v, neighbor))

    # Find the minimum total courier routes cost
    total_cost = 0
    for a, b in routes:
        total_cost += distances[a]

    # Return the minimum total courier routes cost
    return total_cost

