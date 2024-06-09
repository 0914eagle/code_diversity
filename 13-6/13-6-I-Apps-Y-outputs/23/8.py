
def get_optimal_solution(N, p, estimations):
    # Sort the estimations in non-decreasing order
    estimations.sort()
    
    # Initialize the number of accepted problems and penalty time
    num_ac = 0
    penalty_time = 0
    
    # Loop through the estimations and add the problems one by one
    for i in range(N):
        # If the current problem is the first problem to solve, skip it
        if i == p:
            continue
        # If the current problem cannot be solved within the remaining time, break the loop
        if estimations[i] > 300 - penalty_time:
            break
        # Add the current problem to the list of accepted problems
        num_ac += 1
        # Update the penalty time
        penalty_time += estimations[i]
    
    # Return the number of accepted problems and penalty time
    return num_ac, penalty_time

