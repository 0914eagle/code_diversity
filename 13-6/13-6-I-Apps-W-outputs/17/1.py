
def get_max_segments(arr, k):
    # Calculate the number of segments with XOR not equal to 0
    segments = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] ^ arr[j] != 0:
                segments += 1
    
    # If k is 1, return the number of segments
    if k == 1:
        return segments
    
    # Initialize the maximum number of segments with XOR not equal to 0
    max_segments = segments
    
    # Iterate over the array and calculate the number of segments with XOR not equal to 0 after applying the operation
    for i in range(len(arr)):
        # Calculate the number of segments with XOR not equal to 0 after applying the operation
        segments_after_operation = 0
        for j in range(len(arr)):
            if i == j:
                continue
            if arr[i] ^ arr[j] != 0:
                segments_after_operation += 1
        
        # Update the maximum number of segments with XOR not equal to 0
        max_segments = max(max_segments, segments_after_operation)
    
    return max_segments

