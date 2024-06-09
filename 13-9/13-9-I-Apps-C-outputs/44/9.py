
def find_optimal_flight(n, flights):
    # Initialize a graph with the given flights
    graph = {i: set() for i in range(1, n + 1)}
    for i, j in flights:
        graph[i].add(j)
        graph[j].add(i)

    # Find the flight with the maximum number of changes
    max_changes = 0
    flight_to_cancel = None
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if len(graph[i] & graph[j]) == 0:
                num_changes = len(graph[i]) + len(graph[j]) - 2
                if num_changes > max_changes:
                    max_changes = num_changes
                    flight_to_cancel = (i, j)

    # Find the best new flight to add
    new_flight = None
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if (i, j) != flight_to_cancel and (j, i) not in graph:
                new_flight = (i, j)
                break
        if new_flight:
            break

    return max_changes, flight_to_cancel, new_flight

