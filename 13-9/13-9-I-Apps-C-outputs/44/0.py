
def get_optimal_flight_change(n, flights):
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

    # Find the best new flight to add
    min_connections = n
    new_flight = None
    for i in range(n - 1):
        for j in range(n - 1):
            if i != j and graph[i][j] == 0:
                connections = 0
                for k in range(n - 1):
                    if graph[i][k] == 1 and graph[k][j] == 1:
                        connections += 1
                if connections < min_connections:
                    min_connections = connections
                    new_flight = (i + 1, j + 1)

    return (max_connections - min_connections + 1, flight_to_cancel, new_flight)

