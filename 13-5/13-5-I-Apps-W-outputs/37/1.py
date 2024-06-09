
def get_min_time(n, a, b):
    # Initialize the minimum time to wait at each crossing
    min_time = [0] * n

    # Loop through each crossing
    for i in range(n):
        # Get the waiting time for the current crossing
        waiting_time = a[i]

        # If the current crossing is not the last crossing
        if i != n - 1:
            # Get the waiting time for the next crossing
            next_waiting_time = a[i + 1]

            # If the waiting time for the next crossing is greater than the current waiting time
            if next_waiting_time > waiting_time:
                # Update the minimum time to wait at the current crossing
                min_time[i] = next_waiting_time

        # If the current crossing is not the first crossing
        if i != 0:
            # Get the waiting time for the previous crossing
            prev_waiting_time = a[i - 1]

            # If the waiting time for the previous crossing is greater than the current waiting time
            if prev_waiting_time > waiting_time:
                # Update the minimum time to wait at the current crossing
                min_time[i] = prev_waiting_time

    # Return the sum of the minimum time to wait at each crossing
    return sum(min_time)

