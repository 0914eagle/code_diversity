
def solve(n, d, a, m):
    # Sort the hook prices in ascending order
    sorted_hooks = sorted(a)

    # Initialize the total profit to 0
    total_profit = 0

    # Loop through each guest
    for i in range(m):
        # If the guest can use an available hook, add the hook price to the total profit
        if sorted_hooks[i] <= d:
            total_profit += sorted_hooks[i]
        # Otherwise, pay the fine and do not add the hook price to the total profit
        else:
            total_profit -= d

    # Return the total profit
    return total_profit

