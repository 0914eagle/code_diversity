
def get_maximum_segments(arr, k):
    # Initialize variables
    n = len(arr)
    segments = 0
    xor_sum = 0
    
    # Iterate over the array
    for i in range(n):
        # Calculate the XOR sum of the current segment
        xor_sum ^= arr[i]
        
        # If the XOR sum is not equal to 0, increment the number of segments
        if xor_sum != 0:
            segments += 1
        
        # If we are not at the last element, calculate the XOR sum of the next segment
        if i != n-1:
            xor_sum ^= arr[i+1]
    
    # Return the maximum number of segments
    return segments

