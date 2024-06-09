
def get_maximum_profit(N, F, P):
    # Initialize the maximum profit to 0
    max_profit = 0
    
    # Iterate over each period and day
    for day in range(1, 6):
        for period in range(1, 3):
            # Initialize the profit for this period and day to 0
            profit = 0
            
            # Iterate over each shop
            for shop in range(1, N+1):
                # Check if the shop is open during this period and day
                if F[shop][day][period] == 1:
                    # Add the profit for this shop to the total profit
                    profit += P[shop][period]
            
            # Update the maximum profit if the profit for this period and day is greater than the current maximum profit
            max_profit = max(max_profit, profit)
    
    # Return the maximum profit
    return max_profit
