
def solve(n, m, train_lines):
    # Initialize a graph with the given train lines
    graph = {i: set() for i in range(1, n + 1)}
    for line in train_lines:
        graph[line[0]].add(line[1])
        graph[line[1]].add(line[0])

    # Find all possible routes with the minimum number of flights
    routes = []
    for city in range(1, n + 1):
        route = [city]
        visited = set()
        queue = [city]
        while queue:
            current = queue.pop(0)
            if current not in visited:
                visited.add(current)
                route.append(current)
                queue += list(graph[current] - visited)
        routes.append(route)

    # Find the route with the minimum number of flights
    min_flights = float('inf')
    min_route = []
    for route in routes:
        flights = 0
        for i in range(len(route) - 1):
            if route[i] != route[i + 1]:
                flights += 1
        if flights < min_flights:
            min_flights = flights
            min_route = route

    # Find the airports that can be visited
    airports = set()
    for city in min_route:
        if city in graph[city]:
            airports.add(city)

    return [min_flights, ' '.join(map(str, sorted(airports)))]

