
def solve(n, flights):
    # Initialize a graph with the given flights
    graph = [[] for _ in range(n + 1)]
    for flight in flights:
        graph[flight[0]].append(flight[1])
        graph[flight[1]].append(flight[0])
    
    # Find the flight with the maximum number of connections
    max_connections = 0
    flight_to_cancel = None
    for i in range(1, n + 1):
        connections = 0
        for j in range(1, n + 1):
            if i != j and j in graph[i]:
                connections += 1
        if connections > max_connections:
            max_connections = connections
            flight_to_cancel = i
    
    # Find the city with the maximum number of connections after cancelling the flight
    city_with_max_connections = 0
    max_connections = 0
    for i in range(1, n + 1):
        if i != flight_to_cancel and len(graph[i]) > max_connections:
            max_connections = len(graph[i])
            city_with_max_connections = i
    
    # Find the city with the minimum number of connections after adding a new flight
    city_with_min_connections = 0
    min_connections = n
    for i in range(1, n + 1):
        if i != flight_to_cancel and i != city_with_max_connections and len(graph[i]) < min_connections:
            min_connections = len(graph[i])
            city_with_min_connections = i
    
    # Return the result
    return [max_connections, flight_to_cancel, city_with_max_connections, city_with_min_connections]

