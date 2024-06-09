
def solve(n, c, x):
    # Initialize variables
    max_profit = 0
    barrels = 0
    raspberry = 0

    # Iterate through the prices
    for i in range(n):
        # If the bear has enough raspberry, buy a barrel
        if raspberry >= x[i]:
            barrels += 1
            raspberry -= x[i]

        # If the bear has a barrel and enough raspberry, sell a barrel and lend it to the friend
        if barrels > 0 and raspberry >= c:
            max_profit += x[i]
            barrels -= 1
            raspberry -= c

    return max_profit

