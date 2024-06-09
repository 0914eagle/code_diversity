
def solve(n, m, train_lines):
    # Initialize a graph with the given train lines
    graph = {i: set() for i in range(1, n + 1)}
    for a, b in train_lines:
        graph[a].add(b)
        graph[b].add(a)
    
    # Find all possible routes with the minimum number of flights
    routes = []
    for city in range(1, n + 1):
        route = [city]
        visited = set()
        while len(route) < n:
            next_city = -1
            for neighbor in graph[route[-1]] - visited:
                if neighbor not in route:
                    next_city = neighbor
                    break
            if next_city == -1:
                break
            route.append(next_city)
            visited.add(next_city)
        if len(route) == n:
            routes.append(route)
    
    # Find the routes with the minimum number of flights
    min_flights = float('inf')
    min_routes = []
    for route in routes:
        flights = 0
        for i in range(n - 1):
            if route[i] != route[i + 1]:
                flights += 1
        if flights < min_flights:
            min_flights = flights
            min_routes = [route]
        elif flights == min_flights:
            min_routes.append(route)
    
    # Find the airports that can be visited
    airports = set()
    for route in min_routes:
        for city in route:
            if city in graph[city]:
                airports.add(city)
    
    return [min_flights, ' '.join(map(str, sorted(airports)))]

