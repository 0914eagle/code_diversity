
def get_minimum_lounges(n_airports, n_routes, routes):
    # Initialize a graph with the given number of airports
    graph = [[] for _ in range(n_airports)]

    # Add edges to the graph based on the given routes
    for route in routes:
        graph[route[0] - 1].append(route[1] - 1)
        graph[route[1] - 1].append(route[0] - 1)

    # Initialize a set to store the airports that have a lounge
    lounges = set()

    # Iterate through the graph and find the airports that need a lounge
    for airport in range(n_airports):
        if len(graph[airport]) > 0:
            # If the airport has outgoing edges, it needs a lounge
            lounges.add(airport)
        for neighbor in graph[airport]:
            # If the airport has a neighbor that already has a lounge, it doesn't need a lounge
            if neighbor in lounges:
                lounges.remove(airport)
                break

    # Return the number of lounges needed
    return len(lounges)

def main():
    n_airports, n_routes = map(int, input().split())
    routes = []
    for _ in range(n_routes):
        routes.append(list(map(int, input().split())))
    print(get_minimum_lounges(n_airports, n_routes, routes))

if __name__ == '__main__':
    main()

