
def get_flight_changes(n, flights):
    # Initialize a graph with the given number of cities
    graph = [[] for _ in range(n)]

    # Add edges to the graph based on the given flights
    for flight in flights:
        graph[flight[0] - 1].append(flight[1] - 1)
        graph[flight[1] - 1].append(flight[0] - 1)

    # Find the city with the most connections
    max_connections = 0
    most_connected_city = 0
    for i in range(n):
        connections = len(graph[i])
        if connections > max_connections:
            max_connections = connections
            most_connected_city = i

    # Find the flight to cancel and the new flight to add
    flight_to_cancel = -1
    flight_to_add = -1
    for i in range(n):
        if i != most_connected_city:
            if len(graph[i]) < max_connections - 1:
                flight_to_cancel = i + 1
                flight_to_add = most_connected_city + 1
                break

    return flight_to_cancel, flight_to_add

def main():
    n = int(input())
    flights = []
    for i in range(n - 1):
        flights.append(list(map(int, input().split())))
    flight_to_cancel, flight_to_add = get_flight_changes(n, flights)
    print(flight_to_cancel)
    print(flight_to_add)

if __name__ == '__main__':
    main()

