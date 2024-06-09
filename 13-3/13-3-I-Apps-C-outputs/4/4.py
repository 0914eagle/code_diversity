
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
            # Remove the airport from the graph to prevent it from being visited again
            graph[airport] = []

    # Count the number of lounges needed
    n_lounges = len(lounges)

    # Check if all airports have a lounge
    if n_lounges == n_airports:
        return n_lounges

    # If not, try to add a lounge to each airport that doesn't have one
    for airport in range(n_airports):
        if airport not in lounges:
            # If the airport has outgoing edges, it can have a lounge
            if len(graph[airport]) > 0:
                lounges.add(airport)
                n_lounges += 1

    return n_lounges

def main():
    n_airports, n_routes = map(int, input().split())
    routes = []
    for _ in range(n_routes):
        routes.append(list(map(int, input().split())))
    print(get_minimum_lounges(n_airports, n_routes, routes))

if __name__ == '__main__':
    main()

