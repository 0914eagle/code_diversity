
def get_input():
    n = int(input())
    flights = []
    for i in range(n - 1):
        a, b = map(int, input().split())
        flights.append((a, b))
    return n, flights

def cancel_flight(n, flights):
    # Initialize a graph with n vertices and 0 edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph based on the flights
    for a, b in flights:
        graph[a - 1].append(b - 1)
        graph[b - 1].append(a - 1)

    # Find the flight with the most connections
    max_connections = 0
    flight_to_cancel = 0
    for i in range(n - 1):
        connections = len(graph[i])
        if connections > max_connections:
            max_connections = connections
            flight_to_cancel = i + 1

    return flight_to_cancel

def add_flight(n, flights, flight_to_cancel):
    # Find the city that is not connected to the flight to be canceled
    for a, b in flights:
        if a != flight_to_cancel and b != flight_to_cancel:
            break
    city_to_connect = a if a != flight_to_cancel else b

    # Find the city that is not connected to the flight to be canceled
    for a, b in flights:
        if a != flight_to_cancel and b != flight_to_cancel:
            break
    city_to_connect_to = a if a != flight_to_cancel else b

    return city_to_connect, city_to_connect_to

def main():
    n, flights = get_input()
    flight_to_cancel = cancel_flight(n, flights)
    city_to_connect, city_to_connect_to = add_flight(n, flights, flight_to_cancel)
    print(2)
    print(flight_to_cancel, city_to_connect)
    print(city_to_connect_to, flight_to_cancel)

if __name__ == '__main__':
    main()

