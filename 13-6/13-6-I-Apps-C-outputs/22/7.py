
def get_optimal_flight_changes(n, flights):
    # Initialize a graph with the given flights
    graph = {i: set() for i in range(1, n + 1)}
    for flight in flights:
        graph[flight[0]].add(flight[1])
        graph[flight[1]].add(flight[0])

    # Find the flight with the maximum number of connections
    max_connections = 0
    flight_to_cancel = None
    for flight in flights:
        connections = len(graph[flight[0]]) + len(graph[flight[1]])
        if connections > max_connections:
            max_connections = connections
            flight_to_cancel = flight

    # Find the city with the maximum number of connections
    city_with_max_connections = 0
    max_connections = 0
    for city in range(1, n + 1):
        connections = len(graph[city])
        if connections > max_connections:
            max_connections = connections
            city_with_max_connections = city

    # Find the city that is not in the flight to cancel
    city_to_add = 0
    for city in range(1, n + 1):
        if city not in flight_to_cancel and city != city_with_max_connections:
            city_to_add = city
            break

    return (max_connections - 1, flight_to_cancel[0], flight_to_cancel[1], city_to_add)

