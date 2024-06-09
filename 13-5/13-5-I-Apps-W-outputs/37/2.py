
def get_min_wait_time(n, a, b):
    # Initialize the minimum total wait time to infinity
    min_wait_time = float('inf')
    
    # Loop through all possible paths
    for path in permutations(range(n)):
        # Initialize the total wait time to 0
        total_wait_time = 0
        
        # Loop through the path
        for i in range(n - 1):
            # Get the indices of the current and next house
            curr_house = path[i]
            next_house = path[i + 1]
            
            # Check if the houses are in the same row
            if curr_house // n == next_house // n:
                # Get the waiting time for the current crossing
                wait_time = a[curr_house % n][next_house % n]
            else:
                # Get the waiting time for the current crossing
                wait_time = b[curr_house % n]
            
            # Add the waiting time to the total wait time
            total_wait_time += wait_time
        
        # Check if the total wait time is less than the minimum total wait time
        if total_wait_time < min_wait_time:
            # Update the minimum total wait time
            min_wait_time = total_wait_time
    
    # Return the minimum total wait time
    return min_wait_time

