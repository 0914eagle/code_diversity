
def solve(arr):
    n = len(arr)
    if n == 1:
        return 0
    
    # Sort the array
    arr.sort()
    
    # Initialize variables
    min_size = float('inf')
    i = 1
    
    # Iterate through the array
    while i < n:
        # If the current element is the same as the previous element, find the length of the subsegment that needs to be removed
        if arr[i] == arr[i-1]:
            j = i + 1
            while j < n and arr[j] == arr[j-1]:
                j += 1
            size = j - i
            if size < min_size:
                min_size = size
        i += 1
    
    return min_size

