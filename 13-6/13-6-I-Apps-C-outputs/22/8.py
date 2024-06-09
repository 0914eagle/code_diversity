
def find_optimal_flight(n, flights):
    # Initialize a graph with the given flights
    graph = {i: set() for i in range(1, n + 1)}
    for flight in flights:
        graph[flight[0]].add(flight[1])
        graph[flight[1]].add(flight[0])

    # Find the flight with the maximum number of changes
    max_changes = 0
    flight_to_cancel = None
    for city in range(1, n + 1):
        for neighbor in graph[city]:
            if len(graph[neighbor]) - 1 > max_changes:
                max_changes = len(graph[neighbor]) - 1
                flight_to_cancel = (city, neighbor)

    # Find the best new flight to add
    best_new_flight = None
    for city in range(1, n + 1):
        if city not in graph[flight_to_cancel[0]] and city not in graph[flight_to_cancel[1]]:
            best_new_flight = (flight_to_cancel[0], city)
            break

    return (max_changes, flight_to_cancel, best_new_flight)

