
def solve(n, times):
    # Sort the times in non-decreasing order
    times.sort()
    # Initialize the total time required
    total_time = 0
    # Iterate over the teams
    for i in range(n):
        # Add the time required for the current team
        total_time += times[i]
        # If it is not the last team, add the time required for the pause
        if i != n - 1:
            total_time += 1
    return total_time

