
def solve(N, p, times):
    # Initialize variables
    num_ac = 0
    penalty_time = 0

    # Sort the times in non-decreasing order
    sorted_times = sorted(times)

    # Loop through the problems in non-decreasing order
    for i in range(N):
        # If the current problem is the one that should be solved first, skip it
        if i == p:
            continue
        # If the current problem cannot be solved within the remaining time, break the loop
        if sorted_times[i] > penalty_time:
            break
        # Increment the number of accepted problems and add the time for the current problem to the penalty time
        num_ac += 1
        penalty_time += sorted_times[i]

    # Return the number of accepted problems and the penalty time
    return num_ac, penalty_time

