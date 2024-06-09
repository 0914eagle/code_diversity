
def solve_flight_problem(n, flights):
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
    min_connections = max_connections
    new_flight = None
    for city1 in graph:
        for city2 in graph:
            if city1 != city2 and (city1, city2) not in flights:
                connections = len(graph[city1]) + len(graph[city2])
                if connections < min_connections:
                    min_connections = connections
                    new_flight = (city1, city2)

    return (min_connections, flight_to_cancel, new_flight)

