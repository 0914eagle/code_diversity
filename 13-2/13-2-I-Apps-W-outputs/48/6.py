
def solve(N, K, logs):
    # Sort the logs in non-decreasing order
    logs.sort()
    
    # Initialize the maximum length of a log to 0
    max_length = 0
    
    # Loop through each log and try to cut it at different points
    for i in range(N):
        # Get the length of the current log
        length = logs[i]
        
        # Loop through each possible point to cut the log
        for j in range(1, K+1):
            # Calculate the length of the two logs that will be obtained by cutting the log at the current point
            left_length = length * j / (K+1)
            right_length = length - left_length
            
            # Update the maximum length if the current log is the longest one obtained so far
            if right_length > max_length:
                max_length = right_length
    
    # Return the rounded up value of the maximum length
    return int(math.ceil(max_length))

