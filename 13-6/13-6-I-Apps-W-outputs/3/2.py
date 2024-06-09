
def max_points(n, k, M, t):
    # Sort the subtask times in non-decreasing order
    t.sort()
    
    # Initialize the maximum points to 0
    max_points = 0
    
    # Iterate over each subtask time
    for i in range(k):
        # Check if the subtask time is less than or equal to the time limit
        if t[i] <= M:
            # Add the points for the subtask to the maximum points
            max_points += 1
            # Subtract the time for the subtask from the time limit
            M -= t[i]
    
    # If the last subtask time is less than or equal to the time limit, add the points for the last subtask
    if t[k-1] <= M:
        max_points += 1
    
    # Return the maximum points
    return max_points

