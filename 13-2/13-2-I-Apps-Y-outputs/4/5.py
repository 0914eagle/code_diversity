
def is_sorted(arr):
    # Sort the array in non-decreasing order
    arr.sort()
    
    # Initialize a variable to keep track of the previous height
    prev_height = 0
    
    # Iterate through the array and check if the current height is greater than or equal to the previous height
    for height in arr:
        if height < prev_height:
            return "NO"
        prev_height = height
    
    # If all heights are non-decreasing, return "YES"
    return "YES"

