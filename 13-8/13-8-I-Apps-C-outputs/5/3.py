
def solve(arr):
    n = len(arr)
    if n == 1:
        return 0
    
    # Sort the array
    arr.sort()
    
    # Initialize variables
    min_removals = n
    curr_removals = 0
    
    # Iterate through the array
    for i in range(n-1):
        if arr[i] == arr[i+1]:
            curr_removals += 1
        else:
            min_removals = min(min_removals, curr_removals)
            curr_removals = 0
    
    # Check if the last element is duplicates
    if arr[n-1] == arr[n-2]:
        min_removals = min(min_removals, 1)
    
    return min_removals

