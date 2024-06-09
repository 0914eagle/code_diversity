
def is_sorted(arr):
    # Sort the array in non-decreasing order
    arr.sort()
    
    # Initialize a variable to keep track of the height of the tallest stack
    tallest_stack = 0
    
    # Loop through the array and check if the height of the stack is greater than the tallest stack
    for i in range(len(arr)):
        if arr[i] > tallest_stack:
            tallest_stack = arr[i]
    
    # If the tallest stack is not the last element in the array, return "NO"
    if tallest_stack != arr[-1]:
        return "NO"
    
    # Otherwise, return "YES"
    return "YES"

