
def get_min_time(n, a, b):
    # Initialize the minimum time to wait at each crossing
    min_time = [0] * n

    # Loop through each row
    for i in range(n):
        # Loop through each crossing in the current row
        for j in range(n - 1):
            # Get the waiting time for the current crossing
            waiting_time = a[i][j]

            # If the current crossing is not the first or last crossing in the row
            if j > 0 and j < n - 2:
                # Add the waiting time for the previous crossing to the current waiting time
                waiting_time += min_time[j - 1]

            # If the current crossing is the first or last crossing in the row
            else:
                # Add the waiting time for the previous crossing to the current waiting time
                waiting_time += min_time[j]

            # Update the minimum time to wait at the current crossing
            min_time[j] = waiting_time

    # Return the minimum total time to wait at the crossings
    return sum(min_time)

