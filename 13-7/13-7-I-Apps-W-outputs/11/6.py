
def solve(n, c, x):
    # Initialize variables
    max_profit = 0
    barrels = 0
    raspberry = 0

    # Loop through the days
    for i in range(n):
        # If the bear has enough raspberry, buy a barrel
        if raspberry >= c:
            barrels += 1
            raspberry -= c

        # If the bear has enough barrels, sell a barrel
        if barrels > 0:
            max_profit += x[i] - c
            barrels -= 1

    return max_profit

