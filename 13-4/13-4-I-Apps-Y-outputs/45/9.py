
def get_earliest_time(x):
    # Initialize the time variable
    time = 1

    # Loop until the kangaroo reaches the nest
    while x > 0:
        # Check if the kangaroo can jump to the left or right
        if x % time == 0:
            # Jump to the left
            x -= time
        else:
            # Jump to the right
            x += time

        # Increment the time
        time += 1

    # Return the earliest time
    return time - 1

