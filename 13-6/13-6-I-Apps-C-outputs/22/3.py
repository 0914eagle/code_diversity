
def find_best_flight_changes(n, flights):
    # Initialize a graph with the given flights
    graph = {i: set() for i in range(1, n + 1)}
    for flight in flights:
        graph[flight[0]].add(flight[1])
        graph[flight[1]].add(flight[0])

    # Find the flight with the maximum number of connections
    max_connections = 0
    flight_to_cancel = None
    for flight in graph:
        connections = len(graph[flight])
        if connections > max_connections:
            max_connections = connections
            flight_to_cancel = flight

    # Find the best new flight to add
    flight_to_add = None
    for city in graph[flight_to_cancel]:
        if len(graph[city]) < max_connections:
            flight_to_add = city
            break

    return (max_connections - 1, flight_to_cancel, flight_to_add)

