
def solve(n, a, b, c):
    # Initialize the sum of satisfaction points
    satisfaction_points = 0
    
    # Iterate over the dishes
    for i in range(n):
        # Add the satisfaction points gained from eating the current dish
        satisfaction_points += b[i]
        
        # If the current dish is not the last dish, add the satisfaction points gained from eating the next dish
        if i < n - 1:
            satisfaction_points += c[i]
    
    return satisfaction_points

