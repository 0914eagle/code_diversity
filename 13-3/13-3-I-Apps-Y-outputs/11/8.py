
def solve(N, T):
    # Initialize a list to store the times when the hands point upward
    upward_times = []
    
    # Loop through each clock
    for i in range(N):
        # Calculate the time when the hand of the current clock points upward
        upward_time = (i + 1) * T
        
        # Add the time to the list
        upward_times.append(upward_time)
    
    # Return the minimum time needed for all hands to point upward
    return min(upward_times)

