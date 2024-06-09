
def get_minimum_lounges(n_airports, n_routes, routes):
    # Initialize a graph with the given number of airports
    graph = [[] for _ in range(n_airports)]

    # Add edges to the graph based on the given routes
    for route in routes:
        graph[route[0] - 1].append(route[1] - 1)
        graph[route[1] - 1].append(route[0] - 1)

    # Initialize a set to keep track of the airports that have a lounge
    lounges = set()

    # Initialize a variable to keep track of the minimum number of lounges needed
    min_lounges = 0

    # Loop through each airport in the graph
    for airport in range(n_airports):
        # If the airport has not been visited yet, visit it and mark it as visited
        if airport not in lounges:
            # Initialize a queue to do a BFS traversal of the graph starting from the current airport
            queue = [airport]

            # Loop through the queue until it is empty
            while queue:
                # Dequeue a node from the queue
                node = queue.pop(0)

                # If the node has not been visited yet, visit it and mark it as visited
                if node not in lounges:
                    # Add the node to the set of airports with a lounge
                    lounges.add(node)

                    # Enqueue the neighbors of the node that have not been visited yet
                    for neighbor in graph[node]:
                        if neighbor not in lounges:
                            queue.append(neighbor)

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

    # Print the minimum number of lounges needed
    print(min_lounges)

if __name__ == '__main__':
    main()

