
def get_min_time(n, a, b):
    # Initialize the minimum time to wait at each crossing
    min_time = [0] * n

    # Loop through each row
    for i in range(n):
        # Loop through each crossing in the current row
        for j in range(n - 1):
            # Get the waiting time for the current crossing
            waiting_time = a[i][j]

            # Check if the current crossing is in the first or second row
            if i == 0 or i == n - 1:
                # Add the waiting time to the minimum time at the current crossing
                min_time[j] += waiting_time
            else:
                # Get the waiting time for the opposite crossing
                opposite_crossing = n - 1 - j

                # Check if the minimum time at the opposite crossing has already been set
                if min_time[opposite_crossing] == 0:
                    # Set the minimum time at the opposite crossing to the waiting time
                    min_time[opposite_crossing] = waiting_time
                else:
                    # Add the waiting time to the minimum time at the opposite crossing
                    min_time[opposite_crossing] += waiting_time

    # Return the sum of the minimum times at all crossings
    return sum(min_time)

