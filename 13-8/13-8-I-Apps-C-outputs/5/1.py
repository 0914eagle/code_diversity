
def solve(arr):
    n = len(arr)
    if n == 1:
        return 0
    
    # Sort the array
    arr.sort()
    
    # Initialize variables for the minimum size of the subsegment to remove
    min_size = 0
    min_idx = 0
    
    # Iterate through the array
    for i in range(n-1):
        # Check if the current element is equal to the next element
        if arr[i] == arr[i+1]:
            # If it is, update the minimum size and index
            min_size = max(min_size, i+1)
            min_idx = i
    
    # If the minimum size is non-zero, return it
    if min_size > 0:
        return min_size
    
    # Otherwise, return 0
    return 0

