
def get_minimum_lounges(n_airports, n_routes, routes):
    # Initialize a graph with the given number of airports
    graph = [[] for _ in range(n_airports)]

    # Add edges to the graph based on the given routes
    for route in routes:
        graph[route[0] - 1].append(route[1] - 1)
        graph[route[1] - 1].append(route[0] - 1)

    # Initialize a set to store the airports that have a lounge
    lounges = set()

    # Iterate through the graph and find the airports that have a lounge
    for airport in range(n_airports):
        if any(route[2] > 0 for route in routes if route[0] - 1 == airport or route[1] - 1 == airport):
            lounges.add(airport)

    # Initialize a set to store the airports that are connected to a lounge
    connected_airports = set()

    # Iterate through the graph and find the airports that are connected to a lounge
    for airport in range(n_airports):
        if any(route[2] > 0 for route in routes if route[0] - 1 == airport or route[1] - 1 == airport):
            connected_airports.add(airport)
            for neighbor in graph[airport]:
                if neighbor not in connected_airports:
                    connected_airports.add(neighbor)

    # Return the number of lounges needed to connect all the airports
    return len(connected_airports)

def main():
    n_airports, n_routes = map(int, input().split())
    routes = []
    for _ in range(n_routes):
        routes.append(list(map(int, input().split())))
    print(get_minimum_lounges(n_airports, n_routes, routes))

if __name__ == '__main__':
    main()

