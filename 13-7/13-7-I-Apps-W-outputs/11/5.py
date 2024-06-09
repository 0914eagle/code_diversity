
def solve(n, c, x):
    # Initialize the maximum profit and the day to sell the honey
    max_profit = 0
    day_to_sell = 0
    
    # Loop through each day
    for i in range(n):
        # Calculate the profit if the bear sells the honey on the current day
        profit = x[i] - c
        
        # If the profit is greater than the current maximum profit, update the maximum profit and the day to sell the honey
        if profit > max_profit:
            max_profit = profit
            day_to_sell = i
    
    # Return the maximum profit
    return max_profit

