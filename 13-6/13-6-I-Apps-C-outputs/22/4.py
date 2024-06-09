
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
    min_changes = float("inf")
    new_flight = None
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if i not in graph[j] and j not in graph[i]:
                changes = len(graph[i] & graph[j]) + 1
                if changes < min_changes:
                    min_changes = changes
                    new_flight = (i, j)

    return (max_changes - 1, flight_to_cancel, new_flight)

