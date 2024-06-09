
def get_earliest_time(x):
    # Initialize the earliest time to reach the nest as 0
    earliest_time = 0

    # Loop through the possible jump lengths from 1 to x
    for jump_length in range(1, x + 1):
        # Calculate the time it takes to reach the nest with the current jump length
        time_taken = (x - 1) // jump_length + 1

        # If the time taken is less than the earliest time, update the earliest time
        if time_taken < earliest_time:
            earliest_time = time_taken

    # Return the earliest time
    return earliest_time

