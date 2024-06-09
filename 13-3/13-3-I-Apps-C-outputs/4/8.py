
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
        # If the airport has not been visited yet, visit it and its neighbors
        if airport not in lounges:
            # Mark the airport as visited
            lounges.add(airport)

            # Loop through the neighbors of the airport
            for neighbor in graph[airport]:
                # If the neighbor has not been visited yet, visit it and its neighbors
                if neighbor not in lounges:
                    # Mark the neighbor as visited
                    lounges.add(neighbor)

                    # Increment the minimum number of lounges needed
                    min_lounges += 1

    # Return the minimum number of lounges needed
    return min_lounges

def main():
    # Read the number of airports and routes
    n_airports, n_routes = map(int, input().split())

    # Read the routes
    routes = []
    for _ in range(n_routes):
        routes.append(list(map(int, input().split())))

    # Call the function to get the minimum number of lounges needed
    min_lounges = get_minimum_lounges(n_airports, n_routes, routes)

    # Print the result
    print(min_lounges)

if __name__ == '__main__':
    main()

