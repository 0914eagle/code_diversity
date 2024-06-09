
def solve(n, A, B, C):
    # Initialize the satisfaction points to 0
    satisfaction_points = 0
    
    # Loop through each dish
    for i in range(n):
        # Add the satisfaction points gained from eating the current dish
        satisfaction_points += B[i]
        
        # If the current dish is not the last dish, add the satisfaction points gained from eating the next dish
        if i != n - 1:
            satisfaction_points += C[i]
    
    # Return the total satisfaction points
    return satisfaction_points

