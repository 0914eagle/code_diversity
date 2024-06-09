
def get_max_profit(n, a, d, c):
    # Calculate the gap between each pair of problems
    gaps = [0] + [max(d[i + 1] - d[i], 0) for i in range(n - 1)]
    # Initialize the maximum profit and the current profit
    max_profit, curr_profit = 0, 0
    # Iterate through the problems and calculate the maximum profit
    for i in range(n):
        # Add the current problem to the contest
        curr_profit += a
        # Add the gap between the current problem and the next problem
        curr_profit += gaps[i]
        # Update the maximum profit if necessary
        max_profit = max(max_profit, curr_profit - c[i])
    # Return the maximum profit
    return max_profit
