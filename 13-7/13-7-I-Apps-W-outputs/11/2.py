
def solve(n, c, prices):
    # Initialize variables
    max_profit = 0
    barrels = 0
    raspberries = 0

    # Iterate through the prices
    for i in range(n):
        # If the bear has enough raspberries, buy a barrel
        if raspberries >= prices[i]:
            barrels += 1
            raspberries -= prices[i]

        # If the bear has a barrel and enough raspberries, sell the barrel and earn profit
        if barrels > 0 and raspberries >= c:
            max_profit += prices[i]
            barrels -= 1
            raspberries += c

    return max_profit

