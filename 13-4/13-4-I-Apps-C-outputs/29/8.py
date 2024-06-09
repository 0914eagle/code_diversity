
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
            if route not in train_routes and route not in bus_routes:
                train_routes.append(route)
                bus_routes.append(route)

    # Find the maximum arrival time for the bus and the train
    max_bus_arrival = 0
    max_train_arrival = 0
    for route in bus_routes:
        max_bus_arrival = max(max_bus_arrival, len(route) - 1)
    for route in train_routes:
        max_train_arrival = max(max_train_arrival, len(route) - 1)

    # Return the maximum of the two arrival times
    return max(max_bus_arrival, max_train_arrival)

def find_routes(graph, start, end):
    # Base case: if we reach the end node, return the route
    if start == end:
        return [[start]]

    # Initialize an empty route and explore all neighbors
    routes = []
    for neighbor in graph[start]:
        for route in find_routes(graph, neighbor, end):
            routes.append([start] + route)

    return routes

