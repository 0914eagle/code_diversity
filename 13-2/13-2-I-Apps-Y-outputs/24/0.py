
def solve(n, times):
    # Sort the times in non-decreasing order
    times.sort()

    # Initialize the minimum time required for Ante and Goran to do their lectures
    min_time = 0

    # Iterate over the teams
    for i in range(n):
        # Add the time required for the current team to understand and implement an algorithm
        min_time += times[i]

        # If Ante and Goran are not working with the same team, add the time required for them to switch
        if i % 2 == 0:
            min_time += 1

    return min_time

