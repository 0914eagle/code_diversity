
def solve(n, c, x):
    # Initialize variables
    max_profit = 0
    barrels = 0
    raspberry = 0

    # Iterate over the days
    for i in range(n):
        # If the bear has enough raspberry, buy a barrel
        if raspberry >= x[i]:
            barrels += 1
            raspberry -= x[i]

        # If the bear has enough barrels and raspberry, sell a barrel
        if barrels > 0 and raspberry + c <= x[i]:
            max_profit = max(max_profit, barrels * x[i] - raspberry)
            barrels -= 1
            raspberry += x[i]

    return max_profit

