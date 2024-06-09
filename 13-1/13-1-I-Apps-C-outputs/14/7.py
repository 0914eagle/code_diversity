
def get_min_cost(n, m, roads):
    # Initialize the graph with the given roads
    graph = {i: set() for i in range(1, n + 1)}
    for a, b in roads:
        graph[a].add(b)
        graph[b].add(a)

    # Initialize the cost of each area to 0
    costs = [0] * (n + 1)

    # Initialize the visited array to keep track of visited areas
    visited = [False] * (n + 1)

    # Function to recursively find the minimum cost of decorating the city
    def dfs(area, parent):
        # Mark the current area as visited
        visited[area] = True

        # If the current area is not the starting area, check if the cost is valid
        if area != 1:
            # Get the cost of the parent area
            parent_cost = costs[parent]

            # Get the cost of the current area
            current_cost = costs[area]

            # Check if the sum of the costs is odd
            if (parent_cost + current_cost) % 3 == 1:
                return -1

        # Recursively call the function for all the adjacent areas
        for adjacent in graph[area]:
            if not visited[adjacent]:
                result = dfs(adjacent, area)
                if result == -1:
                    return -1

        return costs[area]

    # Call the dfs function for the starting area
    result = dfs(1, 0)

    # If the result is -1, it means that it's not possible to decorate the city according to Peter's properties
    if result == -1:
        return -1

    # Otherwise, return the minimum cost
    return result

