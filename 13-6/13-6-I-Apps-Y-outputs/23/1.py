
def solve(N, p, times):
    # Sort the times in non-decreasing order
    sorted_times = sorted(times)

    # Initialize the number of accepted problems and penalty time
    num_ac = 0
    penalty_time = 0

    # Loop through each problem in the sorted times
    for i in range(N):
        # If the current problem is the first problem to be solved
        if i == p:
            # Add the time for the current problem to the penalty time
            penalty_time += sorted_times[i]
        # If the current problem is not the first problem to be solved
        else:
            # Check if the current problem can be solved within the remaining time
            if sorted_times[i] <= 300 - penalty_time:
                # Add the time for the current problem to the penalty time
                penalty_time += sorted_times[i]
                # Increment the number of accepted problems
                num_ac += 1
            # If the current problem cannot be solved within the remaining time
            else:
                # Break out of the loop
                break

    # Return the number of accepted problems and penalty time
    return num_ac, penalty_time

