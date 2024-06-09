
def solve(n, c, a, b):
    # Initialize the minimum time to reach each floor as infinity
    min_time = [float('inf')] * (n + 1)
    # The minimum time to reach the first floor is 0
    min_time[1] = 0

    # Loop through each floor
    for i in range(1, n + 1):
        # Loop through each possible next floor
        for j in range(1, n + 1):
            # Calculate the time to reach the next floor using the stairs
            stairs_time = min_time[i] + a[j - 1]
            # Calculate the time to reach the next floor using the elevator
            elevator_time = min_time[i] + c + b[j - 1]
            # Update the minimum time to reach the next floor
            min_time[j] = min(stairs_time, elevator_time)

    return min_time[1:]

