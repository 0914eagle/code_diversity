
def read_input():
    n = int(input())
    flights = []
    for i in range(n - 1):
        a, b = map(int, input().split())
        flights.append((a, b))
    return n, flights

def find_optimal_flight(n, flights):
    # Initialize a graph with n vertices and 0 edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph
    for a, b in flights:
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)

    # Find the flight with the maximum number of connections
    max_connections = 0
    flight_to_cancel = None
    for i in range(n - 1):
        connections = len(graph[i])
        if connections > max_connections:
            max_connections = connections
            flight_to_cancel = i + 1

    # Find the city with the maximum number of connections
    max_connections = 0
    city_to_add = None
    for i in range(n):
        connections = len(graph[i])
        if connections > max_connections:
            max_connections = connections
            city_to_add = i + 1

    return flight_to_cancel, city_to_add

def main():
    n, flights = read_input()
    flight_to_cancel, city_to_add = find_optimal_flight(n, flights)
    print(flight_to_cancel)
    print(city_to_add)

if __name__ == '__main__':
    main()

