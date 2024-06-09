
def solve(arr):
    n = len(arr)
    if n == 1:
        return 0
    
    # Sort the array
    arr.sort()
    
    # Initialize variables
    min_size = float('inf')
    start = 0
    end = 1
    
    # Iterate through the array
    for i in range(1, n):
        # If the current element is the same as the previous element, update the start and end indices
        if arr[i] == arr[i-1]:
            start = i
        # If the current element is different from the previous element, check if the subsegment is valid
        else:
            # Check if the subsegment is valid
            if is_valid_subsegment(arr, start, i):
                # Update the minimum size if necessary
                min_size = min(min_size, i - start + 1)
            # Update the start index
            start = i
    
    # Check the last subsegment
    if is_valid_subsegment(arr, start, n-1):
        min_size = min(min_size, n - start)
    
    return min_size

def is_valid_subsegment(arr, start, end):
    # Check if the subsegment is valid
    for i in range(start, end+1):
        for j in range(i+1, end+1):
            if arr[i] == arr[j]:
                return False
    return True

