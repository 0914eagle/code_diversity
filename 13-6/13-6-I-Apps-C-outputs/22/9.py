
def find_best_flight(n, flights):
    # Initialize a graph with the given flights
    graph = {i: set() for i in range(1, n + 1)}
    for flight in flights:
        graph[flight[0]].add(flight[1])
        graph[flight[1]].add(flight[0])

    # Find the flight with the maximum number of connections
    max_connections = 0
    flight_to_cancel = None
    for flight in flights:
        connections = 0
        for city in graph[flight[0]]:
            if city in graph[flight[1]]:
                connections += 1
        if connections > max_connections:
            max_connections = connections
            flight_to_cancel = flight

    # Find the best new flight to add
    new_flight = None
    for city in graph[flight_to_cancel[0]]:
        if city not in graph[flight_to_cancel[1]]:
            new_flight = (flight_to_cancel[0], city)
            break
    if new_flight is None:
        for city in graph[flight_to_cancel[1]]:
            if city not in graph[flight_to_cancel[0]]:
                new_flight = (flight_to_cancel[1], city)
                break

    return (max_connections - 1, flight_to_cancel, new_flight)

