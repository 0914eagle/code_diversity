
def solve(N, K, logs):
    # Sort the logs in non-decreasing order
    logs.sort()
    
    # Initialize the maximum length of a log to 0
    max_length = 0
    
    # Loop through each log and try to cut it at different points
    for i in range(N):
        # Get the length of the current log
        length = logs[i]
        
        # Loop through each possible cut point (0 to length - 1)
        for j in range(K + 1):
            # Calculate the length of the two logs that will be created by cutting the current log at point j
            left_length = j
            right_length = length - j
            
            # If the sum of the lengths of the two logs is greater than the maximum length, update the maximum length
            if left_length + right_length > max_length:
                max_length = left_length + right_length
    
    # Return the maximum length rounded up to the nearest integer
    return int(math.ceil(max_length))

