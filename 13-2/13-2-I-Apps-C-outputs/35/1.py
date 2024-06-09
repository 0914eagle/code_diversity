
def speedrun(n, r, m, tricks):
    # Initialize the variables
    expected_time = 0
    current_time = 0
    num_resets = 0

    # Loop through each trick in the route
    for trick in tricks:
        t, p, d = trick

        # If the trick occurs before the current time, reset the game
        if t < current_time:
            num_resets += 1
            current_time = 0

        # If the trick occurs after the current time, update the current time
        if t > current_time:
            current_time = t

        # Calculate the expected time to recover from the trick
        expected_recovery_time = d * (1 - p)

        # Add the expected time to recover from the trick to the expected time
        expected_time += expected_recovery_time

    # Calculate the expected time to set a new record
    expected_time += n - current_time

    # Return the expected time to set a new record
    return expected_time

