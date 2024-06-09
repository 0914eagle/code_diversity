
def get_earliest_time(x):
    # Initialize variables
    time = 1
    position = 0

    # Loop until the kangaroo reaches the nest
    while position != x:
        # Check if the kangaroo can jump to the left or right
        if position + time < x:
            position += time
        elif position - time >= 0:
            position -= time
        else:
            time += 1

    # Return the earliest possible time
    return time

