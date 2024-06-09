
def find_best_flight(n, flights):
    # Initialize a graph with n vertices and 0 edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph based on the given flights
    for flight in flights:
        graph[flight[0] - 1].append(flight[1] - 1)
        graph[flight[1] - 1].append(flight[0] - 1)

    # Find the flight with the maximum number of connections
    max_connections = 0
    flight_to_cancel = None
    for i in range(n - 1):
        connections = 0
        for j in range(n - 1):
            if i != j and graph[i][j] == 1:
                connections += 1
        if connections > max_connections:
            max_connections = connections
            flight_to_cancel = i + 1

    # Find the city with the minimum number of connections
    min_connections = n
    city_to_add = None
    for i in range(n - 1):
        connections = 0
        for j in range(n - 1):
            if graph[i][j] == 1:
                connections += 1
        if connections < min_connections:
            min_connections = connections
            city_to_add = i + 1

    return [max_connections, flight_to_cancel, city_to_add]

