
def get_earliest_time_to_reach_x(x):
    # Initialize the earliest time to be the maximum possible value
    earliest_time = float('inf')
    
    # Iterate through all possible jump lengths
    for jump_length in range(1, x + 1):
        # Calculate the time it takes to reach the nest with the current jump length
        time = x // jump_length
        
        # If the time is less than the earliest time, update the earliest time
        if time < earliest_time:
            earliest_time = time
    
    return earliest_time

