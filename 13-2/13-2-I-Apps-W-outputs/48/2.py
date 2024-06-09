
def solve(N, K, A):
    # Sort the logs in non-decreasing order
    A.sort()
    
    # Initialize the maximum length of a log
    max_length = 0
    
    # Loop through each log
    for i in range(N):
        # Calculate the length of the current log
        length = A[i]
        
        # Loop through each possible cut
        for j in range(K+1):
            # Calculate the length of the first log
            first_length = length * j / (K+1)
            
            # Calculate the length of the second log
            second_length = length - first_length
            
            # Update the maximum length if necessary
            max_length = max(max_length, first_length, second_length)
    
    # Return the rounded up maximum length
    return int(math.ceil(max_length))

