
def find_optimal_flight_change(n, flights):
    # Initialize a graph with the given flights
    graph = {i: set() for i in range(1, n + 1)}
    for i, j in flights:
        graph[i].add(j)
        graph[j].add(i)

    # Find the flight with the maximum number of connections
    max_connections = 0
    flight_to_cancel = None
    for i in range(1, n + 1):
        connections = 0
        for j in graph[i]:
            if i != j:
                connections += len(graph[j])
        if connections > max_connections:
            max_connections = connections
            flight_to_cancel = i

    # Find the best new flight to add
    min_connections = float('inf')
    flight_to_add = None
    for i in range(1, n + 1):
        if i != flight_to_cancel and len(graph[i]) < min_connections:
            min_connections = len(graph[i])
            flight_to_add = i

    return max_connections, flight_to_cancel, flight_to_add

def main():
    n = int(input())
    flights = []
    for _ in range(n - 1):
        flights.append(tuple(map(int, input().split())))
    max_connections, flight_to_cancel, flight_to_add = find_optimal_flight_change(n, flights)
    print(max_connections)
    print(*flight_to_cancel, flight_to_add)

if __name__ == '__main__':
    main()

