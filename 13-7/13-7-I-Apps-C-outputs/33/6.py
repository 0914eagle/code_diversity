
def get_input():
    n = int(input())
    flights = []
    for i in range(n - 1):
        a, b = map(int, input().split())
        flights.append((a, b))
    return n, flights

def get_flight_changes(n, flights):
    # Initialize a graph with the flights as edges
    graph = [[] for _ in range(n + 1)]
    for a, b in flights:
        graph[a].append(b)
        graph[b].append(a)
    
    # Find the city with the most connections
    city_connections = [len(graph[i]) for i in range(1, n + 1)]
    city_with_most_connections = city_connections.index(max(city_connections))
    
    # Find the city that is not connected to the city with the most connections
    cities_to_consider = [i for i in range(1, n + 1) if i != city_with_most_connections]
    min_flight_changes = float('inf')
    flight_to_cancel = None
    new_flight = None
    for city_to_connect in cities_to_consider:
        # Find the city that is not connected to the city to connect
        city_to_disconnect = [i for i in range(1, n + 1) if i not in graph[city_to_connect]][0]
        
        # Cancel the flight from city_to_disconnect to city_to_connect
        graph[city_to_disconnect].remove(city_to_connect)
        graph[city_to_connect].remove(city_to_disconnect)
        
        # Add a new flight from city_to_disconnect to city_with_most_connections
        graph[city_to_disconnect].append(city_with_most_connections)
        graph[city_with_most_connections].append(city_to_disconnect)
        
        # Count the number of flight changes needed
        flight_changes = 0
        for i in range(1, n + 1):
            if i != city_with_most_connections:
                flight_changes += len(graph[i]) - 1
        
        # If the number of flight changes is less than the minimum, update the minimum and the flight to cancel and the new flight
        if flight_changes < min_flight_changes:
            min_flight_changes = flight_changes
            flight_to_cancel = (city_to_disconnect, city_to_connect)
            new_flight = (city_to_disconnect, city_with_most_connections)
    
    # Return the minimum number of flight changes, the flight to cancel, and the new flight
    return min_flight_changes, flight_to_cancel, new_flight

def main():
    n, flights = get_input()
    min_flight_changes, flight_to_cancel, new_flight = get_flight_changes(n, flights)
    print(min_flight_changes)
    print(*flight_to_cancel)
    print(*new_flight)

if __name__ == '__main__':
    main()

