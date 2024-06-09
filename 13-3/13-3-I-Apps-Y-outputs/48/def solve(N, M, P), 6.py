
def solve(N, M, P):
    # Initialize the time required for each swather to be completed
    time_required = [0] * N
    
    # Initialize the time at which each swather is completed
    time_completed = [0] * N
    
    # Loop through each stage
    for stage in range(M):
        # Loop through each swather
        for swather in range(N):
            # Check if the swather is not already completed
            if time_completed[swather] == 0:
                # Add the time required for the current stage to the time required for the swather
                time_required[swather] += P[swather][stage]
                
                # Check if the swather is completed in the current stage
                if time_required[swather] >= time_completed[swather]:
                    # Update the time at which the swather is completed
                    time_completed[swather] = time_required[swather]
    
    # Return the time at which each swather is completed
    return time_completed

