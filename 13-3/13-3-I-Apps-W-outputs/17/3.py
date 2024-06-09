
def solve(n, m, a):
    # Initialize the graph with the given fridges and weights
    graph = {i: set() for i in range(1, n + 1)}
    for i in range(1, n + 1):
        graph[i] = set(range(1, n + 1))
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            graph[i].add(j)
            graph[j].add(i)
    for i in range(1, n + 1):
        graph[i].remove(i)

    # Initialize the cost of each fridge to be its weight
    cost = {i: a[i - 1] for i in range(1, n + 1)}

    # Initialize the number of chains to be 0
    num_chains = 0

    # Loop until all fridges are private or no more chains can be created
    while num_chains < m and len(graph) > 0:
        # Find the fridge with the minimum cost
        min_cost = float("inf")
        for i in graph:
            if cost[i] < min_cost:
                min_cost = cost[i]
                min_fridge = i

        # Remove the minimum fridge from the graph
        graph.pop(min_fridge)

        # Update the cost of the remaining fridges
        for i in graph:
            cost[i] -= min_cost

        # Increment the number of chains
        num_chains += 1

    # If all fridges are private, return the cost, otherwise return -1
    if len(graph) == 0:
        return cost
    else:
        return -1

