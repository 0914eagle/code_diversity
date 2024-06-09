
def solve(n, m, k, roads, routes):
    # Initialize a graph with the given roads
    graph = {i: set() for i in range(1, n + 1)}
    for road in roads:
        x, y, cost = road
        graph[x].add((y, cost))
        graph[y].add((x, cost))

    # Find the shortest path between each pair of districts using Dijkstra's algorithm
    distances = {i: float("inf") for i in range(1, n + 1)}
    previous = {i: None for i in range(1, n + 1)}
    queue = [(0, 1)]
    while queue:
        dist, node = heapq.heappop(queue)
        if distances[node] < dist:
            continue
        for neighbor, cost in graph[node]:
            new_dist = dist + cost
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                previous[neighbor] = node
                heapq.heappush(queue, (new_dist, neighbor))

    # Calculate the total cost of each route
    total_cost = 0
    for route in routes:
        x, y = route
        total_cost += distances[x] + distances[y]

    return total_cost

