
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
    max_bus_time = 0
    max_train_time = 0
    for route in bus_routes:
        max_bus_time = max(max_bus_time, len(route))
    for route in train_routes:
        max_train_time = max(max_train_time, len(route))

    # Return the maximum of the two arrival times
    return max(max_bus_time, max_train_time)

def find_routes(graph, start, end):
    # Base case: if we have reached the end node, return the current path
    if start == end:
        return [[start]]

    # Initialize an empty list to store the paths
    paths = []

    # Iterate over all neighbors of the current node
    for neighbor in graph[start]:
        # Find all paths from the neighbor to the end node
        for path in find_routes(graph, neighbor, end):
            # Add the current node to the beginning of the path
            paths.append([start] + path)

    return paths

