
def get_min_hours(n, m, railways):
    # Initialize a graph with the given railways
    graph = {i: set() for i in range(1, n + 1)}
    for u, v in railways:
        graph[u].add(v)
        graph[v].add(u)

    # Find all possible routes for the train and the bus
    train_routes = []
    bus_routes = []
    for i in range(1, n + 1):
        for route in dfs(graph, i):
            if len(route) == n:
                train_routes.append(route)
            if len(route) == n - 1:
                bus_routes.append(route)

    # Find the minimum hours needed for the train and the bus to reach town n
    min_hours_train = float("inf")
    min_hours_bus = float("inf")
    for route in train_routes:
        hours = 0
        for i in range(len(route) - 1):
            u, v = route[i], route[i + 1]
            hours += 1
        min_hours_train = min(min_hours_train, hours)
    for route in bus_routes:
        hours = 0
        for i in range(len(route) - 1):
            u, v = route[i], route[i + 1]
            hours += 1
        min_hours_bus = min(min_hours_bus, hours)

    # Return the maximum of the minimum hours needed for the train and the bus
    return max(min_hours_train, min_hours_bus)


def dfs(graph, start):
    visited = set()
    stack = [(start, [start])]
    while stack:
        node, path = stack.pop()
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))
    return [path for node, path in visited.items() if node != start]

