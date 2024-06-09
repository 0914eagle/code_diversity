
def solve(n, flights):
    # Initialize a graph with the given flights
    graph = {i: set() for i in range(1, n + 1)}
    for i, j in flights:
        graph[i].add(j)
        graph[j].add(i)

    # Find the flight with the maximum number of connections
    max_connections = 0
    flight_to_cancel = None
    for i in range(1, n + 1):
        connections = len(graph[i])
        if connections > max_connections:
            max_connections = connections
            flight_to_cancel = i

    # Find the city with the minimum number of connections
    min_connections = n
    city_to_add = None
    for i in range(1, n + 1):
        connections = len(graph[i])
        if connections < min_connections:
            min_connections = connections
            city_to_add = i

    return (max_connections - 1, flight_to_cancel, city_to_add)

