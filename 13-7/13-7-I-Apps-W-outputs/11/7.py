
def max_raspberry(n, c, x):
    # Initialize variables
    max_profit = 0
    barrel_price = 0
    raspberry_left = 0

    # Iterate through each day
    for i in range(n):
        # Check if the bear has enough raspberry to lend a barrel
        if raspberry_left >= c:
            # Calculate the profit if the bear lends a barrel on this day
            profit = x[i] - barrel_price - c

            # Check if the profit is positive
            if profit > 0:
                # Update the maximum profit
                max_profit = max(max_profit, profit)

                # Update the raspberry left and the price of the barrel
                raspberry_left -= c
                barrel_price = x[i]

    # Return the maximum profit
    return max_profit

