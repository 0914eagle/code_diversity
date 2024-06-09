
def speedrun(n, r, m, tricks):
    # Initialize variables
    expected_time = 0
    current_time = 0
    num_resets = 0

    # Loop through the tricks
    for trick in tricks:
        t, p, d = trick
        # If the trick occurs before the current time, add its duration to the current time
        if t <= current_time:
            current_time += d
            num_resets += 1
        # If the trick occurs after the current time, calculate the expected time until the trick
        else:
            # Calculate the probability of success and the expected time until the trick
            prob_success = p
            expected_time_until_trick = (t - current_time) / prob_success
            # Add the expected time until the trick to the total expected time
            expected_time += expected_time_until_trick
            # Increment the current time by the duration of the trick
            current_time = t + d

    # Calculate the expected time to set a new record
    expected_time_to_set_record = expected_time + num_resets * (r - n)

    return expected_time_to_set_record

