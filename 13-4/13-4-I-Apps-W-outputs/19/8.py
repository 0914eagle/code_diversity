
def solve(n, d, a, m):
    # Sort the hook prices in non-decreasing order
    sorted_hooks = sorted(a)
    # Initialize the total profit to 0
    total_profit = 0
    # Loop through each guest
    for i in range(m):
        # If there are no available hooks, pay the fine
        if len(sorted_hooks) == 0:
            total_profit -= d
        # Otherwise, choose the cheapest available hook and remove it from the list
        else:
            total_profit += sorted_hooks[0]
            sorted_hooks = sorted_hooks[1:]
    # Return the total profit
    return total_profit

