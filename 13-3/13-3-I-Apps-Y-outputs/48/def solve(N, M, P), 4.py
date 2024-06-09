
def solve(N, M, P):
    # Initialize the time required for each swather to be completed
    time_required = [0] * N
    # Initialize the time at which each swather is completed
    time_completed = [0] * N
    # Initialize the current time
    current_time = 0
    # Loop through each stage
    for stage in range(M):
        # Loop through each swather
        for swather in range(N):
            # Check if the swather is ready to be processed at this stage
            if time_required[swather] == stage:
                # Add the time required for this stage to the current time
                current_time += P[swather][stage]
                # Update the time required for this swather to be completed
                time_required[swather] += 1
                # Update the time at which this swather is completed
                time_completed[swather] = current_time
    # Return the time at which each swather is completed
    return time_completed

