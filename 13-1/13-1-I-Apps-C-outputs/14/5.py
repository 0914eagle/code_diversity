
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

    # Function to check if a cycle exists in the graph
    def has_cycle(start):
        visited[start] = True
        for neighbor in graph[start]:
            if not visited[neighbor]:
                if has_cycle(neighbor):
                    return True
            elif neighbor != start:
                return True
        visited[start] = False
        return False

    # Function to get the minimum cost of decorating the graph
    def get_min_cost_util(start, cost):
        # If the current cost is already odd, return the cost
        if cost % 2 == 1:
            return cost

        # If the current area is already visited, return the cost
        if visited[start]:
            return cost

        # Mark the current area as visited
        visited[start] = True

        # Recursively call the function for all the neighbors of the current area
        for neighbor in graph[start]:
            if not visited[neighbor]:
                cost = get_min_cost_util(neighbor, cost)

        # If a cycle exists in the graph, return -1
        if has_cycle(start):
            return -1

        # Add the cost of the current area to the total cost
        costs[start] = cost

        # Return the updated cost
        return cost + 1

    # Call the function to get the minimum cost of decorating the graph
    cost = get_min_cost_util(1, 0)

    # If a cycle exists in the graph, return -1
    if has_cycle(1):
        return -1

    # Return the minimum cost of decorating the graph
    return cost

