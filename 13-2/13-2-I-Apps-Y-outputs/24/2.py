
def solve(n, times):
    # Sort the times in non-decreasing order
    times.sort()
    # Initialize the total time to 0
    total_time = 0
    # Iterate over the times in pairs
    for i in range(n - 1):
        # Calculate the time difference between the current and next time
        time_diff = times[i + 1] - times[i]
        # If the time difference is greater than 1, add 1 to the total time
        if time_diff > 1:
            total_time += 1
        # Add the current time to the total time
        total_time += times[i]
    # Return the total time
    return total_time

