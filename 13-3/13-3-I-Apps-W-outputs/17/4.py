
def solve(n, m, a):
    # Initialize the minimum total cost to infinity
    cost = float('inf')
    # Initialize the solution with -1
    solution = -1

    # Iterate over all possible combinations of fridges
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            # Check if the combination is valid
            if i != j and a[i - 1] + a[j - 1] <= m:
                # Calculate the total cost of the combination
                total_cost = a[i - 1] + a[j - 1]
                # Check if the total cost is less than the current minimum
                if total_cost < cost:
                    # Update the minimum total cost and the solution
                    cost = total_cost
                    solution = [i, j]

    # Return the solution
    return solution

