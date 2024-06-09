
def get_earliest_time(x):
    # Initialize the time variable
    time = 1

    # Loop until the kangaroo reaches the nest
    while x > 0:
        # If the kangaroo can jump to the left, do so
        if x - time >= 0:
            x -= time
        # Otherwise, jump to the right
        else:
            x += time
        # Increment the time
        time += 1

    # Return the earliest time
    return time

