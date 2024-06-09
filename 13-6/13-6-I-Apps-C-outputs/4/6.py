
def get_min_time(n, m, railways):
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
            if route[0] == 1 and route[-1] == n:
                train_routes.append(route)
            if route[0] == 1 and route[-1] == n:
                bus_routes.append(route)

    # Find the minimum time needed for the train and the bus to reach town n
    min_time_train = float('inf')
    min_time_bus = float('inf')
    for route in train_routes:
        time = len(route) - 1
        if time < min_time_train:
            min_time_train = time
    for route in bus_routes:
        time = len(route) - 1
        if time < min_time_bus:
            min_time_bus = time

    # Return the maximum of the minimum times needed for the train and the bus
    return max(min_time_train, min_time_bus)

def find_routes(graph, start, end):
    routes = []
    queue = [(start, [start], 0)]
    while queue:
        (vertex, path, time) = queue.pop(0)
        for neighbor in graph[vertex]:
            if neighbor not in path:
                new_path = path + [neighbor]
                new_time = time + 1
                if neighbor == end:
                    routes.append(new_path)
                else:
                    queue.append((neighbor, new_path, new_time))
    return routes

if __name__ == '__main__':
    n, m = map(int, input().split())
    railways = []
    for _ in range(m):
        u, v = map(int, input().split())
        railways.append((u, v))
    print(get_min_time(n, m, railways))

