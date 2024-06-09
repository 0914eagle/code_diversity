
def solve(arr):
    n = len(arr)
    if n == 1:
        return 0
    
    # Sort the array
    arr.sort()
    
    # Initialize variables
    min_size = 0
    i = 1
    
    # Iterate through the array
    while i < n:
        # If the current element is the same as the previous element, update the minimum size
        if arr[i] == arr[i-1]:
            min_size = max(min_size, i - (i-1))
        # If the current element is different from the previous element, update the minimum size
        else:
            min_size = max(min_size, i - (i-1))
        
        # Increment the index
        i += 1
    
    return min_size

