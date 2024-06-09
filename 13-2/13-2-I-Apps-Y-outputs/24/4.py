
def solve(n, times):
    # Sort the times in non-decreasing order
    times.sort()
    # Initialize the total time to 0
    total_time = 0
    # Iterate through the times in pairs
    for i in range(0, n-1, 2):
        # Add the sum of the two times to the total time
        total_time += times[i] + times[i+1]
    # If there is an odd number of teams, add the time for the last team
    if n % 2 == 1:
        total_time += times[n-1]
    # Return the total time
    return total_time

