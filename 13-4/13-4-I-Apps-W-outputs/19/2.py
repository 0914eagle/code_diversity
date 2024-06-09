
def solve(n, d, a, m):
    # Sort the hooks by price in ascending order
    sorted_hooks = sorted(a)
    # Initialize the total profit to 0
    total_profit = 0
    # Loop through each guest
    for i in range(m):
        # If there are no available hooks, pay the fine
        if len(sorted_hooks) == 0:
            total_profit -= d
        # Otherwise, use the hook with the lowest price
        else:
            total_profit += sorted_hooks[0]
            sorted_hooks = sorted_hooks[1:]
    return total_profit

