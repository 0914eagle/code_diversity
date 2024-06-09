
def get_maximum_profit(N, F, P):
    # Initialize the maximum profit to 0
    max_profit = 0
    # Loop over each day and period
    for day in range(1, 6):
        for period in range(1, 3):
            # Initialize the profit for this day and period to 0
            profit = 0
            # Loop over each shop
            for shop in range(1, N+1):
                # Check if the shop is open during this day and period
                if F[shop][day][period] == 1:
                    # Add the profit for this shop to the total profit
                    profit += P[shop][period]
            # If the total profit for this day and period is greater than the maximum profit, update the maximum profit
            if profit > max_profit:
                max_profit = profit
    # Return the maximum profit
    return max_profit

