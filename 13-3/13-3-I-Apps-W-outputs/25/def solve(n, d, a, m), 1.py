
def solve(n, d, a, m):
    # Sort the hook prices in non-decreasing order
    sorted_a = sorted(a)

    # Initialize the total profit to 0
    total_profit = 0

    # Loop through each guest
    for i in range(m):
        # Find the minimum price among the available hooks
        min_price = sorted_a[i]

        # If the minimum price is greater than the fine, pay the fine
        if min_price > d:
            total_profit -= d
        else:
            # Otherwise, pay the minimum price
            total_profit += min_price

    return total_profit

