
def get_earliest_time(x):
    # Initialize the time variable
    time = 1

    # Loop until the kangaroo reaches the nest
    while x > 0:
        # Check if the kangaroo can reach the nest in the current time step
        if x % time == 0:
            # If so, return the current time
            return time
        # Increment the time by 1
        time += 1

    # If the kangaroo cannot reach the nest in the given time, return -1
    return -1

