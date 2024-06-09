
def solve(n, c, a, b):
    # Initialize the minimum time array
    min_time = [0] * (n + 1)

    # Loop through each floor
    for i in range(1, n + 1):
        # Initialize the minimum time to reach the current floor
        min_time[i] = float('inf')

        # Loop through each previous floor
        for j in range(1, i + 1):
            # Calculate the time to reach the current floor using the stairs
            stairs_time = sum(a[j - 1:i])

            # Calculate the time to reach the current floor using the elevator
            elevator_time = c + sum(b[j - 1:i])

            # Update the minimum time to reach the current floor
            min_time[i] = min(min_time[i], min_time[j - 1] + min(stairs_time, elevator_time))

    return min_time[n]

