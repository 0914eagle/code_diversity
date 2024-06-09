
def solve(n, m, a, chains):
    # Initialize the minimum total cost to infinity
    min_cost = float('inf')
    # Initialize the optimal solution
    optimal_solution = []
    # Iterate over all possible combinations of chains
    for combination in chains:
        # Calculate the total cost of the current combination
        cost = sum(a[i - 1] + a[j - 1] for i, j in combination)
        # If the total cost is less than the minimum total cost, update the minimum total cost and the optimal solution
        if cost < min_cost:
            min_cost = cost
            optimal_solution = combination
    # If there is no solution, return -1
    if not optimal_solution:
        return -1
    # Otherwise, return the minimum total cost and the optimal solution
    return min_cost, optimal_solution

