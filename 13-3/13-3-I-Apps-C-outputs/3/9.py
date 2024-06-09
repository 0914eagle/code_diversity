
def speedrun_game(n, r, m, tricks):
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

        # If the trick is successful, update the expected time
        if p == 1:
            expected_time += current_time
        # If the trick is unsuccessful, update the expected time and reset the game
        else:
            expected_time += current_time + d
            num_resets += 1
            current_time = 0

    # Return the expected time and number of resets
    return expected_time, num_resets

