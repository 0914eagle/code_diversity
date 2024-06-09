
def get_max_profit(n, a, d, c):
    # Calculate the gap between each pair of problems
    gaps = [0] + [max((d[i+1] - d[i])**2 for i in range(len(d)-1)) if i < len(d)-1 else 0 for i in range(len(d))]
    
    # Initialize the maximum profit and the current profit
    max_profit = 0
    current_profit = 0
    
    # Iterate through the problems and calculate the maximum profit
    for i in range(len(d)):
        # Add the current problem to the contest
        current_profit += a
        
        # Add the gap between the current problem and the next problem
        current_profit += gaps[i]
        
        # If the current profit is greater than the maximum profit, update the maximum profit
        if current_profit > max_profit:
            max_profit = current_profit
    
    # Return the maximum profit
    return max_profit

