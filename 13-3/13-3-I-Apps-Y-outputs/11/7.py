
def solve(N, T):
    # Initialize a list to store the times when the hands point upward
    upward_times = []
    
    # Loop through each clock
    for i in range(N):
        # Calculate the time when the hand of the current clock points upward
        upward_time = (360 * (i + 1)) // N
        
        # Add the time to the list
        upward_times.append(upward_time)
    
    # Sort the list in ascending order
    upward_times.sort()
    
    # Calculate the minimum time needed for all hands to point upward
    min_time = sum(upward_times)
    
    return min_time

