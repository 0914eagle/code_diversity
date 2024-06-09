
def solve(n, m, train_lines):
    # Initialize a graph with the given train lines
    graph = {i: set() for i in range(1, n + 1)}
    for a, b in train_lines:
        graph[a].add(b)
        graph[b].add(a)
    
    # Find the cities that are not reachable from any other city
    unreachable_cities = set(range(1, n + 1))
    for city in graph:
        unreachable_cities -= graph[city]
    
    # Initialize the minimum number of flights to visit all cities
    min_flights = 0
    
    # Initialize the list of airport cities to visit
    airport_cities = []
    
    # Loop through each city and find the shortest path to all other cities
    for city in range(1, n + 1):
        if city in unreachable_cities:
            continue
        visited_cities = set()
        queue = [city]
        while queue:
            current_city = queue.pop(0)
            if current_city in visited_cities:
                continue
            visited_cities.add(current_city)
            queue += list(graph[current_city] - visited_cities)
        min_flights += 1
        airport_cities.append(city)
    
    return min_flights, " ".join(str(city) for city in airport_cities)

