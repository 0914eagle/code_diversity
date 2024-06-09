
def solve(n, c, x):
    # Initialize variables
    max_profit = 0
    barrel_sold = 0
    barrel_bought = 0

    # Iterate through the days
    for i in range(n):
        # Check if the bear has enough raspberry to lend a barrel
        if c + x[i] <= n:
            # Calculate the profit if the bear lends a barrel on day i
            profit = x[i] - x[i+1] - c

            # Check if the profit is greater than the current maximum profit
            if profit > max_profit:
                # Update the maximum profit and the days when a barrel is sold and bought
                max_profit = profit
                barrel_sold = i
                barrel_bought = i + 1

    # Return the maximum profit
    return max_profit

