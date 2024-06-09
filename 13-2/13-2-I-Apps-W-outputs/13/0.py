
def solve(n, k, c, names, enemies):
    # Initialize the minimum number of groups to infinity
    min_groups = float('inf')
    # Initialize the optimal solution
    optimal_solution = []

    # Iterate over all possible combinations of groups
    for group_size in range(1, n + 1):
        # Check if the current group size is valid
        if group_size > c:
            break
        # Iterate over all possible combinations of groups
        for combination in itertools.combinations(names, group_size):
            # Check if the current combination is valid
            if len(set(combination)) != len(combination):
                continue
            # Check if the current combination is an enemy-free group
            if all(name not in enemies for name in combination):
                # Update the minimum number of groups
                min_groups = min(min_groups, group_size)
                # Add the current combination to the optimal solution
                optimal_solution.append(combination)

    # Return the minimum number of groups and the optimal solution
    return min_groups, optimal_solution

