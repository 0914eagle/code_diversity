
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
    def dfs(node, visited, ship_count):
        # Mark the current node as visited
        visited[node] = True

        # If the current node is not already controlled by the Resistance, add it to the list of controlled planets
        if controlled_planets[ship_count] == 0:
            controlled_planets[ship_count] += 1

        # Recursively explore the graph starting from the current node
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor, visited, ship_count)

    # Iterate over the nodes in the graph
    for node in range(n):
        # If the current node is not already visited, recursively explore the graph starting from the current node
        if not visited[node]:
            dfs(node, [False] * n, 1)

    # Return the list of controlled planets for each ship
    return controlled_planets

