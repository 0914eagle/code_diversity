
def solve(n, m, a):
    # Initialize the graph with the weights of the fridges
    graph = {i: {j: a[j] for j in range(n)} for i in range(n)}

    # Initialize the set of chains to be created
    chains = set()

    # Loop until the required number of chains is created
    while len(chains) < m:
        # Find the unlocked fridge with the minimum weight
        min_weight = float('inf')
        for i in range(n):
            if i not in chains:
                for j in range(n):
                    if j not in chains and graph[i][j] < min_weight:
                        min_weight = graph[i][j]
                        fridge1 = i
                        fridge2 = j

        # Add the chain between the two fridges to the graph
        graph[fridge1][fridge2] = 0
        graph[fridge2][fridge1] = 0
        chains.add((fridge1, fridge2))

    # Calculate the total cost of the chains
    total_cost = sum(graph[i][j] for i in range(n) for j in range(n) if graph[i][j] > 0)

    # Return the total cost if the required number of chains is created, otherwise return -1
    return total_cost if len(chains) == m else -1

