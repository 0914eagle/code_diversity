
def solve(sequence, k):
    n = len(sequence)
    if n == 1:
        return 0
    
    # Sort the sequence in non-decreasing order
    sequence.sort()
    
    # Initialize the minimum difference and the current maximum and minimum elements
    min_diff = float('inf')
    max_element = sequence[0]
    min_element = sequence[0]
    
    # Loop through each element in the sequence
    for i in range(n):
        # If the current element is greater than the maximum element, update the maximum element
        if sequence[i] > max_element:
            max_element = sequence[i]
        
        # If the current element is less than the minimum element, update the minimum element
        if sequence[i] < min_element:
            min_element = sequence[i]
        
        # Calculate the current difference between the maximum and minimum elements
        diff = max_element - min_element
        
        # If the current difference is less than the minimum difference, update the minimum difference
        if diff < min_diff:
            min_diff = diff
    
    # If we can perform the operation an odd number of times, we can make the minimum difference even
    if k % 2 == 1:
        min_diff -= 1
    
    return min_diff

