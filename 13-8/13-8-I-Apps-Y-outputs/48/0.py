
def is_sorted_correctly(arr):
    # Sort the array in non-decreasing order
    arr.sort()
    
    # Initialize a variable to keep track of the current height of the stacks
    current_height = 0
    
    # Loop through the array and check if the stacks are sorted correctly
    for i in range(len(arr)):
        # If the current stack is taller than the previous stack, return "NO"
        if arr[i] > current_height + 2:
            return "NO"
        # Update the current height of the stacks
        current_height = max(current_height, arr[i])
    
    # If all stacks are sorted correctly, return "YES"
    return "YES"

