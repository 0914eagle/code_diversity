
def solve(n, c, a, b):
    # Initialize the minimum time to reach each floor
    min_time = [0] * (n + 1)

    # Loop through each floor
    for i in range(1, n + 1):
        # Loop through each possible move
        for j in range(1, n + 1):
            # Calculate the time to move from the current floor to the destination floor
            time = c + sum(b[j - 1:i]) if j < i else sum(a[j - 1:i])

            # Update the minimum time if the current time is less than the previous minimum time
            if min_time[i] > min_time[j] + time:
                min_time[i] = min_time[j] + time

    return min_time

