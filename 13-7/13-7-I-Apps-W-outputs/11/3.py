
def solve(n, c, prices):
    # Initialize variables
    max_profit = 0
    honey_barrels = 0
    raspberry = 0

    # Iterate through the prices
    for i in range(n):
        # Check if the bear has enough raspberry to lend a barrel
        if raspberry >= c:
            # Lend a barrel and earn the price for it
            honey_barrels += 1
            raspberry -= c
            max_profit += prices[i]

        # Check if the bear has enough raspberry to buy a barrel
        if raspberry < c and honey_barrels > 0:
            # Buy a barrel and return it to the friend
            honey_barrels -= 1
            raspberry += prices[i]

    # Return the maximum profit
    return max_profit

