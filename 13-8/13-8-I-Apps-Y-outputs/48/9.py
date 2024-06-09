
def is_correct_sorting(arr):
    # Sort the array in non-decreasing order
    arr.sort()
    
    # Initialize a variable to keep track of the current height of the stacks
    current_height = 0
    
    # Loop through the array and check if the stacks will slide
    for i in range(len(arr)):
        # If the current height is less than the height of the current stack, the stacks will slide
        if current_height < arr[i]:
            return "NO"
        # Update the current height to the height of the current stack
        current_height = arr[i]
    
    # If the loop completes successfully, the array can be sorted using the described procedure
    return "YES"

