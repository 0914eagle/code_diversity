
def get_min_time(n, a, b):
    # Initialize the minimum time to wait at each crossing
    min_time = [0] * n

    # Loop through each row
    for i in range(n):
        # Loop through each crossing in the current row
        for j in range(n - 1):
            # Get the waiting time for the current crossing
            waiting_time = a[i][j]

            # If we are not in the last row, get the waiting time for the next row
            if i != n - 1:
                waiting_time += a[i + 1][j]

            # Update the minimum time to wait at the current crossing
            min_time[j] = max(min_time[j], waiting_time)

    # Loop through each row
    for i in range(n):
        # Loop through each crossing in the current row
        for j in range(n - 1):
            # Get the waiting time for the current crossing
            waiting_time = b[j]

            # If we are not in the last row, get the waiting time for the next row
            if i != n - 1:
                waiting_time += b[j]

            # Update the minimum time to wait at the current crossing
            min_time[j] = max(min_time[j], waiting_time)

    # Return the sum of the minimum time to wait at each crossing
    return sum(min_time)

