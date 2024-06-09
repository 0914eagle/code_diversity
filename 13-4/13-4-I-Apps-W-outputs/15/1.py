
def get_max_profit(n, a, d, c):
    # Calculate the maximum profit by taking a consecutive segment of tasks
    max_profit = 0
    for i in range(n):
        # Calculate the total earnings for the current segment
        total_earnings = a * sum(c[i:])
        # Calculate the total cost for the current segment
        total_cost = sum(c[i:])
        # Calculate the gap between the current segment and the next segment
        gap = 0
        if i < n - 1:
            gap = (d[i + 1] - d[i]) ** 2
        # Update the maximum profit if the current segment is more profitable
        if total_earnings - total_cost - gap > max_profit:
            max_profit = total_earnings - total_cost - gap
    return max_profit

