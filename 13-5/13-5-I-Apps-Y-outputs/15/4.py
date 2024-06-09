
def solve(n, c, a, b):
    # Initialize the minimum time to reach each floor as infinity
    min_time = [float('inf')] * (n + 1)
    # The minimum time to reach the first floor is 0
    min_time[1] = 0

    # Loop through each floor
    for i in range(1, n + 1):
        # Loop through each possible move
        for j in range(1, n + 1):
            # If the move is from the current floor to a higher floor
            if j > i:
                # Calculate the time to reach the higher floor using the stairs
                stairs_time = min_time[i] + sum(a[k - 1] for k in range(i + 1, j + 1))
                # Calculate the time to reach the higher floor using the elevator
                elevator_time = min_time[i] + c + sum(b[k - 1] for k in range(i + 1, j + 1))
                # Update the minimum time to reach the higher floor
                min_time[j] = min(min_time[j], stairs_time, elevator_time)

    return min_time[1:]

