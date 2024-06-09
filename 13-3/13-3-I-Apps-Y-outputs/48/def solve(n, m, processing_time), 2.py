
def solve(n, m, processing_time):
    # Initialize the time for each swather to 0
    times = [0] * n
    
    # Loop through each stage
    for j in range(m):
        # Loop through each swather
        for i in range(n):
            # If the swather is not already completed, add the processing time for this stage
            if times[i] == 0:
                times[i] += processing_time[i][j]
    
    return times

