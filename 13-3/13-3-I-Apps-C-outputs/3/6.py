
def speedrun_game(n, r, m, tricks):
    # Initialize variables
    expected_time = 0
    current_time = 0
    num_resets = 0

    # Loop through the tricks
    for trick in tricks:
        t, p, d = trick

        # If the trick occurs before the current time, reset the game
        if t < current_time:
            num_resets += 1
            current_time = 0

        # If the trick occurs after the current time, update the current time
        if t > current_time:
            current_time = t

        # Add the time lost if the trick fails
        expected_time += d

        # Add the time gained if the trick succeeds
        expected_time += p * (n - current_time)

    # Add the time lost if the game is not completed
    expected_time += (r - current_time) * (1 - p)

    # Return the expected time
    return expected_time / num_resets

