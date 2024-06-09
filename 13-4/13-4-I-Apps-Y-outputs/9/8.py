
def get_min_cost(n, m, k, roads, routes):
    # Initialize a graph with the given roads
    graph = {i: set() for i in range(1, n + 1)}
    for x, y, w in roads:
        graph[x].add((y, w))
        graph[y].add((x, w))

    # Initialize the minimum cost for each route
    min_cost = [float("inf") for _ in range(k)]

    # Loop through each route
    for i in range(k):
        # Get the current route
        route = routes[i]

        # Initialize the current cost for the route
        current_cost = 0

        # Loop through each pair of districts in the route
        for j in range(len(route) - 1):
            # Get the current and next district
            x, y = route[j], route[j + 1]

            # Find the minimum cost between the current and next district
            min_cost_between = float("inf")
            for neighbor, w in graph[x]:
                if neighbor == y:
                    min_cost_between = min(min_cost_between, w)

            # Add the minimum cost to the current cost
            current_cost += min_cost_between

        # Update the minimum cost for the route
        min_cost[i] = current_cost

    # Return the minimum total cost
    return sum(min_cost)

