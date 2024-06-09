
def solve(N, p, times):
    # Initialize variables
    num_ac = 0
    penalty_time = 0

    # Sort the times in non-decreasing order
    sorted_times = sorted(times)

    # Loop through each problem and calculate the penalty time
    for i in range(N):
        # If the current problem is the first problem to be solved, skip it
        if i == p:
            continue
        # Calculate the penalty time for the current problem
        penalty_time += sorted_times[i]
        # If the penalty time exceeds 300 minutes, break the loop
        if penalty_time > 300:
            break
        # Increment the number of accepted problems
        num_ac += 1

    # Return the number of accepted problems and penalty time
    return num_ac, penalty_time

