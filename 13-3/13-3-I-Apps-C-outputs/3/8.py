
def speedrun(n, r, m, tricks):
    # Initialize variables
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
        elif t > current_time:
            current_time = t
        # If the trick occurs at the current time, calculate the expected time to recover
        else:
            expected_time += d * (1 - p)
            current_time += d

    # Calculate the expected time to set a new record
    expected_time += (r - current_time) / (1 - (1 - p) ** num_resets)

    return expected_time

