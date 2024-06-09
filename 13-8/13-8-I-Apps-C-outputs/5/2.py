
def solve(arr):
    n = len(arr)
    if n == 1:
        return 0
    
    # Sort the array
    arr.sort()
    
    # Initialize variables for the minimum subsegment size and its index
    min_size = float('inf')
    min_index = 0
    
    # Iterate over the array and find the minimum subsegment size
    for i in range(n-1):
        if arr[i] == arr[i+1]:
            size = 2
            while i+size < n and arr[i] == arr[i+size]:
                size += 1
            if size < min_size:
                min_size = size
                min_index = i
    
    return min_size

