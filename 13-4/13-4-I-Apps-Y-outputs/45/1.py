
def find_earliest_time(X):
    # Initialize the time variable
    time = 1

    # Loop until the kangaroo reaches the nest
    while X > 0:
        # Check if the kangaroo can jump to the left or right
        if X - time >= 0:
            X -= time
        else:
            X += time

        # Increment the time
        time += 1

    # Return the earliest possible time
    return time - 1

