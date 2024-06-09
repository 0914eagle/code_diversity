
def is_sorted_correctly(arr):
    # Sort the array in non-decreasing order
    arr.sort()
    
    # Initialize a variable to keep track of the height of the tallest stack
    tallest_stack = 0
    
    # Iterate through the array and check if the stacks are sorted correctly
    for i in range(len(arr) - 1):
        if arr[i] + 1 != arr[i + 1]:
            return "NO"
    
    return "YES"

