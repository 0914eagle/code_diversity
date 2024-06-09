
def get_best_flight_to_cancel_and_new_flight_to_add(n, flights):
    # Initialize a graph with the given flights
    graph = {i: set() for i in range(1, n + 1)}
    for flight in flights:
        graph[flight[0]].add(flight[1])
        graph[flight[1]].add(flight[0])

    # Find the flight with the maximum number of connections
    max_connections = 0
    flight_to_cancel = None
    for flight in flights:
        connections = len(graph[flight[0]] & graph[flight[1]])
        if connections > max_connections:
            max_connections = connections
            flight_to_cancel = flight

    # Find the best new flight to add
    flight_to_add = None
    for city in range(1, n + 1):
        if city not in graph[flight_to_cancel[0]] and city not in graph[flight_to_cancel[1]]:
            flight_to_add = (flight_to_cancel[0], city)
            break

    return (max_connections - 1, flight_to_cancel, flight_to_add)

