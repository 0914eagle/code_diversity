
def get_minimum_lounges(n_airports, n_routes, routes):
    # Initialize a graph with the given number of airports
    graph = [[] for _ in range(n_airports)]

    # Add edges to the graph based on the given routes
    for route in routes:
        graph[route[0] - 1].append(route[1] - 1)
        graph[route[1] - 1].append(route[0] - 1)

    # Initialize a set to store the airports that have a lounge
    lounges = set()

    # Initialize a variable to store the minimum number of lounges needed
    min_lounges = 0

    # Loop through each airport in the graph
    for airport in range(n_airports):
        # If the airport has not been visited yet, visit it and add it to the set of lounges
        if airport not in lounges:
            dfs(graph, airport, lounges)
            min_lounges += 1

    # Return the minimum number of lounges needed
    return min_lounges

def dfs(graph, airport, lounges):
    # If the airport is already in the set of lounges, return
    if airport in lounges:
        return

    # Add the airport to the set of lounges
    lounges.add(airport)

    # Recursively visit the neighbors of the airport
    for neighbor in graph[airport]:
        dfs(graph, neighbor, lounges)

if __name__ == '__main__':
    n_airports, n_routes = map(int, input().split())
    routes = []
    for _ in range(n_routes):
        routes.append(list(map(int, input().split())))
    print(get_minimum_lounges(n_airports, n_routes, routes))

