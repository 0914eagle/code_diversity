
def get_max_controlled_planets(n, tunnels):
    # Initialize a graph with n nodes and 0 edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph based on the tunnels
    for u, v in tunnels:
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)

    # Initialize an array to store the number of controlled planets for each ship
    controlled_planets = [0] * (n + 1)

    # Function to recursively find the maximum number of controlled planets for a given ship
    def dfs(node, ship):
        # If the node has already been visited, return the number of controlled planets
        if controlled_planets[node] > 0:
            return controlled_planets[node]

        # Mark the node as visited and increment the number of controlled planets
        controlled_planets[node] = ship + 1

        # Recursively find the maximum number of controlled planets for each neighbor
        for neighbor in graph[node]:
            controlled_planets[node] = max(controlled_planets[node], dfs(neighbor, ship + 1))

        return controlled_planets[node]

    # Find the maximum number of controlled planets for each ship
    for ship in range(1, n + 1):
        dfs(0, ship)

    # Return the maximum number of controlled planets for each ship
    return controlled_planets

