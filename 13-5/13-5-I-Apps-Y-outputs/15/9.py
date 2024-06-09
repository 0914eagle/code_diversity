
def get_min_time(n, c, a, b):
    # Initialize the minimum time array
    min_time = [0] * (n + 1)

    # Loop through each floor
    for i in range(1, n + 1):
        # Initialize the minimum time to reach the current floor
        min_time[i] = float('inf')

        # Loop through each possible previous floor
        for j in range(i):
            # Calculate the time to reach the current floor using the stairs
            stairs_time = a[j] + min_time[j]

            # Calculate the time to reach the current floor using the elevator
            elevator_time = c + b[j] + min_time[j]

            # Update the minimum time to reach the current floor
            min_time[i] = min(min_time[i], stairs_time, elevator_time)

    return min_time

