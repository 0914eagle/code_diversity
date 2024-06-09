
def get_min_time(n, c, a, b):
    # Initialize the minimum time array
    min_time = [0] * (n + 1)

    # Loop through each floor
    for i in range(1, n + 1):
        # Initialize the minimum time to reach the current floor
        min_time_i = float('inf')

        # Loop through each possible previous floor
        for j in range(i):
            # Calculate the time to reach the current floor using the stairs
            time_stairs = min_time[j] + a[j]

            # Calculate the time to reach the current floor using the elevator
            time_elevator = min_time[j] + c + b[j]

            # Update the minimum time to reach the current floor
            min_time_i = min(min_time_i, time_stairs, time_elevator)

        # Update the minimum time array
        min_time[i] = min_time_i

    return min_time

