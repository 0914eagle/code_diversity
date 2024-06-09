
def get_min_time(n, a, b):
    # Initialize the minimum total time to wait at the crossroads
    min_time = 0

    # Loop through each row
    for i in range(n):
        # Loop through each crossing in the row
        for j in range(n - 1):
            # Add the waiting time for the current crossing to the minimum total time
            min_time += a[i][j]

    # Loop through each crossing in the first row
    for j in range(n):
        # Add the waiting time for the current crossing to the minimum total time
        min_time += b[j]

    # Return the minimum total time
    return min_time

