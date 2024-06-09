
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
        for route in find_all_routes(graph, i, n):
            if len(route) % 2 == 0:
                train_routes.append(route)
            else:
                bus_routes.append(route)

    # Find the maximum arrival time for the bus and the train
    max_bus_arrival = 0
    max_train_arrival = 0
    for route in bus_routes:
        max_bus_arrival = max(max_bus_arrival, len(route) // 2)
    for route in train_routes:
        max_train_arrival = max(max_train_arrival, len(route) // 2)

    # Return the maximum of the two arrival times
    return max(max_bus_arrival, max_train_arrival)

def find_all_routes(graph, start, end):
    routes = []
    for node in graph[start]:
        if node == end:
            routes.append([start, node])
        else:
            for route in find_all_routes(graph, node, end):
                routes.append([start, node] + route)
    return routes

