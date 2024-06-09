
def solve(N, M, processing_time):
    # Initialize the time for each swather to 0
    times = [0] * N
    
    # Loop through each stage
    for stage in range(M):
        # Loop through each swather
        for swather in range(N):
            # If the swather is not already completed
            if times[swather] == 0:
                # Add the processing time for the current stage to the time for the swather
                times[swather] += processing_time[swather][stage]
    
    return times

