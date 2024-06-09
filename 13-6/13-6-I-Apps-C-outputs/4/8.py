
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
        for j in range(i + 1, n + 1):
            if i != j:
                train_routes.append([i, j])
                bus_routes.append([i, j])

    # Remove any routes that use the same railway twice
    for route in train_routes:
        for i in range(len(route) - 1):
            if route[i] in graph[route[i + 1]]:
                train_routes.remove(route)
                break

    # Remove any routes that use the same road twice
    for route in bus_routes:
        for i in range(len(route) - 1):
            if route[i] in graph[route[i + 1]]:
                bus_routes.remove(route)
                break

    # Find the maximum arrival time for the bus and the train
    max_bus_time = 0
    max_train_time = 0
    for route in bus_routes:
        time = len(route)
        if time > max_bus_time:
            max_bus_time = time
    for route in train_routes:
        time = len(route)
        if time > max_train_time:
            max_train_time = time

    # Return the maximum of the two arrival times
    return max(max_bus_time, max_train_time)

def main():
    n, m = map(int, input().split())
    railways = []
    for _ in range(m):
        u, v = map(int, input().split())
        railways.append([u, v])
    print(get_min_time(n, m, railways))

if __name__ == '__main__':
    main()

