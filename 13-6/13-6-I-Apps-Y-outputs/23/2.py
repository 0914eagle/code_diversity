
def solve(N, p, estimations):
    # Sort the estimations in non-decreasing order
    estimations.sort()
    # Initialize the number of accepted problems to 0
    num_ac = 0
    # Initialize the penalty time to 0
    penalty_time = 0
    # Iterate through the estimations
    for i in range(N):
        # If the current problem is the problem that the team wants to solve first
        if i == p:
            # Add the estimated time for the current problem to the penalty time
            penalty_time += estimations[i]
        # If the current problem is not the problem that the team wants to solve first
        else:
            # Add the estimated time for the current problem to the penalty time
            penalty_time += estimations[i]
            # Increment the number of accepted problems
            num_ac += 1
    # Return the number of accepted problems and the penalty time
    return num_ac, penalty_time

