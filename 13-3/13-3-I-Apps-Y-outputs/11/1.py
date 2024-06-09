
def solve(N, T):
    # Initialize a list to store the times when the hands point upward
    upward_times = []
    
    # Iterate through each clock
    for i in range(1, N+1):
        # Calculate the time when the hand of the current clock points upward
        upward_time = T[i-1] * i
        
        # Add the time to the list
        upward_times.append(upward_time)
    
    # Sort the list in ascending order
    upward_times.sort()
    
    # Return the time difference between the first two elements in the list
    return upward_times[1] - upward_times[0]

