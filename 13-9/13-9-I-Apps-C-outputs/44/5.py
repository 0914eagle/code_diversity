
def get_best_flight_changes(flights):
    # Initialize a graph with the given flights
    graph = {i: set() for i in range(1, len(flights) + 1)}
    for flight in flights:
        graph[flight[0]].add(flight[1])
        graph[flight[1]].add(flight[0])

    # Find the flight with the most connections
    max_connections = 0
    flight_to_cancel = None
    for flight, connections in graph.items():
        if len(connections) > max_connections:
            max_connections = len(connections)
            flight_to_cancel = flight

    # Find the best flight to add
    best_flight = None
    min_changes = float('inf')
    for i in range(1, len(flights) + 1):
        for j in range(1, len(flights) + 1):
            if i != j and (i, j) not in flights and (j, i) not in flights:
                changes = 0
                for flight in flights:
                    if flight[0] == i and flight[1] == j:
                        changes += 1
                    elif flight[0] == j and flight[1] == i:
                        changes += 1
                if changes < min_changes:
                    min_changes = changes
                    best_flight = (i, j)

    return (min_changes + 1, flight_to_cancel, best_flight)

