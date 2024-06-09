
def solve(N, p, times):
    # Initialize variables
    num_ac = 0
    penalty_time = 0
    
    # Sort the times in non-decreasing order
    sorted_times = sorted(times)
    
    # Loop through the times and check if the team can solve the problems
    for i in range(N):
        if i == p:
            # If the current problem is the first problem, skip it
            continue
        if sorted_times[i] + penalty_time <= 300:
            # If the current problem can be solved within the time limit, solve it
            num_ac += 1
            penalty_time += sorted_times[i]
        else:
            # If the current problem cannot be solved within the time limit, break the loop
            break
    
    # Return the number of accepted problems and the penalty time
    return num_ac, penalty_time

