
def solve(n, flights):
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
            if len(graph[i] & graph[j]) > max_changes:
                max_changes = len(graph[i] & graph[j])
                flight_to_cancel = (i, j)

    # Find the best new flight to add
    min_changes = max_changes
    new_flight = None
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if i != flight_to_cancel[0] and j != flight_to_cancel[1] and len(graph[i] & graph[j]) < min_changes:
                min_changes = len(graph[i] & graph[j])
                new_flight = (i, j)

    return (min_changes, flight_to_cancel, new_flight)

