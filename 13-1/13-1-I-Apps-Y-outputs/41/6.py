
def solve(N, p, times):
    # Initialize variables
    num_ac = 0
    penalty_time = 0

    # Sort the times in non-decreasing order
    sorted_times = sorted(times)

    # Loop through the problems in non-decreasing order
    for i in range(N):
        # Check if the current problem is the first problem to solve
        if i == p:
            # Add the time for the current problem to the penalty time
            penalty_time += sorted_times[i]
        # Check if the current problem is not the first problem to solve
        elif sorted_times[i] <= penalty_time:
            # Add the time for the current problem to the penalty time
            penalty_time += sorted_times[i]
        # Check if the current problem is not solvable within the time limit
        elif sorted_times[i] > penalty_time + 300:
            # Break the loop and return 0 for the number of accepted problems and penalty time
            return 0, 0
        # Otherwise, the current problem is solvable within the time limit
        else:
            # Increment the number of accepted problems
            num_ac += 1

    # Return the number of accepted problems and penalty time
    return num_ac, penalty_time

