
def solve(N, M, processing_time):
    # Initialize the time for each swather to 0
    time_per_swather = [0] * N
    
    # Loop through each stage
    for stage in range(M):
        # Loop through each swather
        for swather in range(N):
            # If the swather has not been processed yet
            if time_per_swather[swather] == 0:
                # Add the processing time for the current stage to the time for the swather
                time_per_swather[swather] += processing_time[swather][stage]
    
    return time_per_swather

