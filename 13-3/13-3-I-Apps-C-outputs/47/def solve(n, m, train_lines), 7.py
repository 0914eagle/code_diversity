
def solve(n, m, train_lines):
    # Initialize a graph with the given train lines
    graph = {i: set() for i in range(1, n + 1)}
    for line in train_lines:
        graph[line[0]].add(line[1])
        graph[line[1]].add(line[0])

    # Find all possible routes with the minimum number of flights
    routes = []
    for city in graph:
        route = [city]
        visited = set()
        while len(route) < n:
            next_city = graph[route[-1]] - visited
            if not next_city:
                break
            route.append(next_city.pop())
            visited.add(route[-1])
        if len(route) == n:
            routes.append(route)

    # Find the airports that can be visited on any route with the minimum number of flights
    airports = set()
    for route in routes:
        airports.update(route)

    return len(routes), " ".join(str(airport) for airport in sorted(airports))

