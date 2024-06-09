
def solve(n, c, x):
    # Initialize the maximum profit and the day to lend the barrel
    max_profit = 0
    day_to_lend = 0
    
    # Loop through each day
    for d in range(n):
        # Calculate the profit if the bear lends the barrel on the current day
        profit = x[d] - x[d + 1] - c
        
        # If the profit is positive and greater than the current maximum profit, update the maximum profit and the day to lend the barrel
        if profit > 0 and profit > max_profit:
            max_profit = profit
            day_to_lend = d
    
    # Return the maximum profit
    return max_profit

