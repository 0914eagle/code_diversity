
def solve(n, d, a, m):
    # Sort the hook prices in ascending order
    sorted_a = sorted(a)

    # Initialize the total profit to 0
    total_profit = 0

    # Iterate over the number of guests
    for i in range(m):
        # If the guest can hang their clothes on an available hook, add the cost of the hook to the total profit
        if sorted_a[i] <= d:
            total_profit += sorted_a[i]
        # Otherwise, pay the fine and do not add any profit
        else:
            total_profit -= d

    # Return the total profit
    return total_profit

