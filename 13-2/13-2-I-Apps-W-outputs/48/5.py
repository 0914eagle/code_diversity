
def solve(N, K, A):
    # Sort the logs in non-decreasing order
    A.sort()
    
    # Initialize the maximum length of a log
    max_length = 0
    
    # Loop through each log
    for i in range(N):
        # Calculate the length of the current log
        length = A[i]
        
        # Loop through each cut
        for j in range(K):
            # Calculate the distance from the end of the log
            distance = length - j
            
            # Check if the distance is greater than 0
            if distance > 0:
                # Calculate the length of the two logs
                length1 = distance / 2
                length2 = length - length1
                
                # Update the maximum length
                max_length = max(max_length, length1, length2)
    
    # Return the rounded up maximum length
    return int(math.ceil(max_length))

