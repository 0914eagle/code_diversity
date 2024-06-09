
def solve(n, m, train_lines):
    # Initialize a graph with the given train lines
    graph = {i: set() for i in range(1, n + 1)}
    for a, b in train_lines:
        graph[a].add(b)
        graph[b].add(a)
    
    # Find the cities that are not connected to each other
    disconnected_cities = set()
    for city in graph:
        if not graph[city]:
            disconnected_cities.add(city)
    
    # Initialize the minimum number of flights to visit all cities as 0
    min_flights = 0
    
    # Initialize the list of airports to visit as an empty list
    airports = []
    
    # Loop through each city and find the airport
    for city in graph:
        # If the city is not connected to any other city, it is an airport
        if not graph[city]:
            airports.append(city)
        # If the city is connected to at least one other city, it is not an airport
        else:
            # Find the city that is not connected to the current city
            for neighbor in graph[city]:
                if neighbor not in graph[city]:
                    break
            # Add the flight to the minimum number of flights
            min_flights += 1
    
    return min_flights, " ".join(str(airport) for airport in airports)

