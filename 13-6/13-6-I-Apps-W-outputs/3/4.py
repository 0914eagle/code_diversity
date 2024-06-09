
def get_max_points(n, k, M, t):
    # Sort the subtask times in non-decreasing order
    t.sort()
    # Initialize the maximum points to 0
    max_points = 0
    # Iterate over the subtask times
    for i in range(k):
        # Check if the current subtask time is less than or equal to the remaining time
        if t[i] <= M:
            # Update the maximum points
            max_points += 1
            # Subtract the current subtask time from the remaining time
            M -= t[i]
        else:
            # If the current subtask time is greater than the remaining time, break the loop
            break
    # Return the maximum points
    return max_points

