
def get_minimum_cost(n, m, a, chains):
    # Initialize the minimum cost to infinity
    min_cost = float('inf')
    # Initialize the minimum chains to []
    min_chains = []
    # Loop through all possible combinations of chains
    for c in chains:
        # Calculate the total cost of the current combination of chains
        total_cost = sum([a[c[i] - 1] + a[c[i + 1] - 1] for i in range(0, len(c), 2)])
        # If the total cost is less than the minimum cost, update the minimum cost and chains
        if total_cost < min_cost:
            min_cost = total_cost
            min_chains = c
    # Return the minimum cost and chains
    return min_cost, min_chains


def solve_hanhs_apartment(n, m, a):
    # Initialize the list of possible chains to []
    chains = []
    # Loop through all possible combinations of fridges
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            # If the current combination of fridges is not already in the list of possible chains, add it
            if [i, j] not in chains:
                chains.append([i, j])
    # Get the minimum cost and chains for the current combination of fridges
    min_cost, min_chains = get_minimum_cost(n, m, a, chains)
    # If the minimum cost is less than or equal to the total number of fridges, return the minimum cost and chains
    if min_cost <= n:
        return min_cost, min_chains
    # Otherwise, return -1
    else:
        return -1, []

