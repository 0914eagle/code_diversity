
def solve(N, M, processing_time):
    # Initialize the time required for each swather to be completed
    time_required = [0] * N
    # Initialize the current time
    current_time = 0
    # Loop through each stage
    for stage in range(M):
        # Loop through each swather
        for swather in range(N):
            # Check if the swather is ready to be processed at this stage
            if processing_time[swather][stage] > 0:
                # Add the time required for this stage to the current time
                current_time += processing_time[swather][stage]
                # Update the time required for this swather to be completed
                time_required[swather] = current_time
                # Reset the current time to 0
                current_time = 0
    return time_required

