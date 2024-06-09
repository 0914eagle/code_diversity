
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
        for route in find_routes(graph, i, n):
            if len(route) % 2 == 0:
                train_routes.append(route)
            else:
                bus_routes.append(route)

    # Find the maximum arrival time for the bus and the train
    max_bus_arrival = 0
    max_train_arrival = 0
    for route in bus_routes:
        max_bus_arrival = max(max_bus_arrival, len(route))
    for route in train_routes:
        max_train_arrival = max(max_train_arrival, len(route))

    # Return the maximum of the two arrival times
    if max_bus_arrival == 0 or max_train_arrival == 0:
        return -1
    else:
        return max(max_bus_arrival, max_train_arrival)

def find_routes(graph, start, end):
    queue = [(start, [start])]
    while queue:
        node, path = queue.pop(0)
        for neighbor in graph[node]:
            if neighbor not in path:
                new_path = path + [neighbor]
                if neighbor == end:
                    yield new_path
                else:
                    queue.append((neighbor, new_path))

