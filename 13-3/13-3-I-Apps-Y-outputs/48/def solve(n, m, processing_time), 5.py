
def solve(n, m, processing_time):
    # Initialize the time required for each swather to be completed
    time_required = [0] * n
    # Initialize the time at which each swather is completed
    time_completed = [0] * n
    # Initialize the current time
    current_time = 0
    # Loop through each stage
    for stage in range(m):
        # Loop through each swather
        for swather in range(n):
            # Check if the swather is ready to be processed at this stage
            if time_required[swather] == stage:
                # Add the processing time for this stage
                time_required[swather] += processing_time[swather][stage]
                # Update the time at which the swather is completed
                time_completed[swather] = max(time_completed[swather], current_time + processing_time[swather][stage])
        # Update the current time
        current_time = max(time_completed)
    return time_completed

