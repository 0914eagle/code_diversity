
def solve(n, m, a):
    # Initialize the graph with the given fridges and weights
    graph = {i: set() for i in range(1, n + 1)}
    for i in range(1, n + 1):
        graph[i] = set(range(1, n + 1)) - {i}
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j:
                graph[i].add(j)
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j:
                graph[i].add(j)
    
    # Initialize the cost of each chain to be the sum of the weights of the fridges it connects
    cost = {(i, j): a[i - 1] + a[j - 1] for i in range(1, n + 1) for j in range(1, n + 1) if i != j}
    
    # Initialize the number of chains for each fridge to be 0
    num_chains = {i: 0 for i in range(1, n + 1)}
    
    # Initialize the set of fridges that are not private
    non_private_fridges = set(range(1, n + 1))
    
    # Loop until there are no more non-private fridges
    while non_private_fridges:
        # Find the fridge with the minimum number of chains
        min_chains_fridge = min(non_private_fridges, key=lambda x: num_chains[x])
        
        # If the minimum number of chains is greater than m, then there is no solution
        if num_chains[min_chains_fridge] > m:
            return -1
        
        # Add a chain to the minimum number of chains fridge
        non_private_fridges.remove(min_chains_fridge)
        num_chains[min_chains_fridge] += 1
        
        # Update the cost of the chain
        for neighbor in graph[min_chains_fridge]:
            cost[(min_chains_fridge, neighbor)] -= a[min_chains_fridge - 1]
        
        # Update the number of chains for each fridge
        for neighbor in graph[min_chains_fridge]:
            num_chains[neighbor] += 1
    
    # Return the minimum total cost
    return sum(cost.values())

