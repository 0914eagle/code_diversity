
def solve(N, M, processing_time):
    # Initialize the time for each swather to be completed
    time_completed = [0] * N
    
    # Initialize the current stage for each swather
    current_stage = [0] * N
    
    # Initialize the time for each stage to be completed
    time_completed_stage = [0] * M
    
    # Loop through each swather
    for i in range(N):
        # Loop through each stage
        for j in range(M):
            # If the current stage is not completed, continue to the next stage
            if time_completed_stage[j] == 0:
                continue
            
            # If the current stage is completed, update the time completed for the swather
            time_completed[i] = time_completed_stage[j]
            
            # Update the current stage for the swather
            current_stage[i] = j + 1
            
            # Break out of the loop if the swather is completed
            if current_stage[i] == M:
                break
    
    return time_completed

