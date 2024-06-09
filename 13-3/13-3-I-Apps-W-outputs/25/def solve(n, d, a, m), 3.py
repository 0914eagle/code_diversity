
def solve(n, d, a, m):
    # Sort the hook prices in non-decreasing order
    a.sort()
    # Initialize the total profit to 0
    total_profit = 0
    # Loop through each guest
    for i in range(m):
        # If there are no available hooks, pay the fine
        if len(a) == 0:
            total_profit -= d
        # Otherwise, use the least expensive hook and remove it from the list
        else:
            total_profit += a[0]
            a.pop(0)
    # Return the total profit
    return total_profit

