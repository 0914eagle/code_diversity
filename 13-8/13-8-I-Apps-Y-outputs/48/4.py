
def is_sorted_correctly(arr):
    # First, sort the array in non-decreasing order
    arr.sort()
    
    # Initialize a variable to keep track of the height of the tallest stack
    tallest_stack = 0
    
    # Iterate through the array and check if any two adjacent stacks differ in height by 2 or more
    for i in range(len(arr) - 1):
        if arr[i] - arr[i+1] >= 2:
            return "NO"
        tallest_stack = max(tallest_stack, arr[i])
    
    # If we reach this point, the array can be sorted correctly
    return "YES"

