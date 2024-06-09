
def get_min_time(n, a, b):
    # Initialize the minimum time to wait at each crossing
    min_time = [0] * n

    # Loop through each row
    for i in range(n):
        # Loop through each crossing in the current row
        for j in range(n - 1):
            # Get the waiting time for the current crossing
            waiting_time = a[i][j]

            # If the current crossing is not the last crossing in the row
            if j != n - 2:
                # Add the waiting time to the minimum time at the next crossing
                min_time[j + 1] += waiting_time

    # Loop through each row
    for i in range(n):
        # Loop through each crossing in the current row
        for j in range(n - 1):
            # Get the waiting time for the current crossing
            waiting_time = b[j]

            # If the current crossing is not the last crossing in the row
            if j != n - 2:
                # Add the waiting time to the minimum time at the next crossing
                min_time[j + 1] += waiting_time

    # Return the minimum total time
    return sum(min_time)

