
def get_max_controlled_planets(n, tunnels):
    # Initialize a graph with n nodes and 0 edges
    graph = [[] for _ in range(n)]

    # Add edges to the graph
    for u, v in tunnels:
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)

    # Initialize a list to store the number of controlled planets for each ship
    controlled_planets = [0] * (n + 1)

    # Function to recursively find the number of controlled planets for a given ship
    def dfs(node, parent, controlled):
        # If the current node is not the parent and is not already controlled, mark it as controlled and increment the number of controlled planets
        if node != parent and not controlled[node]:
            controlled[node] = True
            controlled_planets[1] += 1

        # Recursively call the function for all the neighbors of the current node
        for neighbor in graph[node]:
            if neighbor != parent:
                dfs(neighbor, node, controlled)

    # Call the dfs function for each node in the graph
    for node in range(n):
        dfs(node, -1, [False] * n)

    # Return the list of number of controlled planets for each ship
    return controlled_planets

