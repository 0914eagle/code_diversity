
def solve(arr):
    n = len(arr)
    if n == 1:
        return 0
    
    # Sort the array
    arr.sort()
    
    # Initialize variables
    min_removal = 0
    current_removal = 0
    previous_element = arr[0]
    
    # Iterate through the array
    for i in range(1, n):
        current_element = arr[i]
        if current_element == previous_element:
            current_removal += 1
        else:
            min_removal = max(min_removal, current_removal)
            current_removal = 0
        previous_element = current_element
    
    # Handle the last element
    min_removal = max(min_removal, current_removal)
    
    return min_removal

