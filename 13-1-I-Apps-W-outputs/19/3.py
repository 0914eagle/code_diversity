
def get_max_controlled_planets(n, tunnels):
    # Initialize a graph with n nodes and 0 edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph based on the tunnels
    for u, v in tunnels:
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)

    # Initialize an array to store the number of controlled planets for each ship
    controlled_planets = [0] * (n + 1)

    # Function to recursively find the number of controlled planets for a given ship
    def dfs(node, parent, controlled_planets):
        # If the node has already been visited, return the number of controlled planets
        if controlled_planets[node] != 0:
            return controlled_planets[node]

        # If the node is not connected to the parent, return 0
        if node not in graph[parent]:
            return 0

        # Recursively find the number of controlled planets for the child nodes
        for child in graph[node]:
            if child != parent:
                controlled_planets[node] += dfs(child, node, controlled_planets)

        # Return the number of controlled planets for the current node
        return controlled_planets[node]

    # Find the maximum number of controlled planets for each ship
    for k in range(1, n + 1):
        controlled_planets[k] = dfs(0, -1, controlled_planets)

    # Return the maximum number of controlled planets for each ship
    return controlled_planets

