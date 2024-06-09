
def get_max_controlled_planets(n, tunnels):
    # Initialize a graph with n nodes and 0 edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph
    for tunnel in tunnels:
        graph[tunnel[0] - 1].append(tunnel[1] - 1)
        graph[tunnel[1] - 1].append(tunnel[0] - 1)

    # Initialize a list to store the number of controlled planets for each ship
    controlled_planets = [0] * (n + 1)

    # Function to recursively find the number of controlled planets for a given ship
    def dfs(node, parent, controlled_planets):
        # If the node is already controlled, return the number of controlled planets
        if controlled_planets[node] > 0:
            return controlled_planets[node]

        # If the node is not controlled, mark it as controlled and recurse on its neighbors
        controlled_planets[node] = 1
        for neighbor in graph[node]:
            if neighbor != parent:
                controlled_planets[node] += dfs(neighbor, node, controlled_planets)

        return controlled_planets[node]

    # Call the dfs function for each ship
    for ship in range(n):
        dfs(ship, -1, controlled_planets)

    # Return the maximum number of controlled planets
    return max(controlled_planets)

