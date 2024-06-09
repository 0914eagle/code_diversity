
def solve_ncpp_airways(n, flights):
    # Initialize a graph with the given flights
    graph = {i: set() for i in range(1, n + 1)}
    for flight in flights:
        graph[flight[0]].add(flight[1])
        graph[flight[1]].add(flight[0])

    # Find the flight with the maximum number of connections
    max_connections = 0
    flight_to_cancel = None
    for city in graph:
        connections = len(graph[city])
        if connections > max_connections:
            max_connections = connections
            flight_to_cancel = city

    # Find the best new flight to add
    min_connections = float('inf')
    flight_to_add = None
    for city in graph:
        if city != flight_to_cancel:
            connections = len(graph[city])
            if connections < min_connections:
                min_connections = connections
                flight_to_add = city

    return (max_connections - 1, flight_to_cancel, flight_to_add)

