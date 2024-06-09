
def speedrun(n, r, m, tricks):
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
        elif t > current_time:
            current_time = t
        # If the trick occurs at the current time, check if it succeeds
        else:
            if p >= 0.5:
                current_time += d
            else:
                num_resets += 1
                current_time = 0

    # Calculate the expected time to set a new record
    expected_time = (n - current_time) / (1 - (num_resets * (1 - p)))

    return expected_time

