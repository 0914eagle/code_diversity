
def get_min_time(n, a, b):
    # Initialize the minimum time to wait at each crossing
    min_time = [0] * n

    # Loop through each row
    for i in range(n):
        # Loop through each crossing in the current row
        for j in range(n - 1):
            # Get the waiting time for the current crossing
            waiting_time = a[i - 1][j]

            # Check if the current crossing is in the same row as the store
            if i == 0:
                # If the current crossing is in the same row as the store, add the waiting time to the minimum time
                min_time[j] += waiting_time
            else:
                # If the current crossing is in a different row, find the previous crossing in the same row
                prev_crossing = j
                while prev_crossing >= 0 and a[i - 1][prev_crossing] == 0:
                    prev_crossing -= 1

                # If there is a previous crossing in the same row, add the waiting time to the minimum time
                if prev_crossing >= 0:
                    min_time[prev_crossing] += waiting_time

    # Loop through each row
    for i in range(n):
        # Loop through each crossing in the current row
        for j in range(n - 1):
            # Get the waiting time for the current crossing
            waiting_time = b[j]

            # Check if the current crossing is in the same row as the store
            if i == 0:
                # If the current crossing is in the same row as the store, add the waiting time to the minimum time
                min_time[j] += waiting_time
            else:
                # If the current crossing is in a different row, find the previous crossing in the same row
                prev_crossing = j
                while prev_crossing >= 0 and a[i - 1][prev_crossing] == 0:
                    prev_crossing -= 1

                # If there is a previous crossing in the same row, add the waiting time to the minimum time
                if prev_crossing >= 0:
                    min_time[prev_crossing] += waiting_time

    # Return the minimum total time
    return sum(min_time)

