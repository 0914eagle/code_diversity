
def is_sorted(arr):
    # Sort the array in descending order
    arr.sort(reverse=True)
    # Initialize a variable to keep track of the height of the tallest stack
    tallest_stack = 0
    # Loop through the array and check if the stacks are sorted correctly
    for i in range(len(arr) - 1):
        # If the current stack is taller than the previous stack, return "NO"
        if arr[i] - arr[i + 1] > 1:
            return "NO"
        # If the current stack is taller than the tallest stack, update the tallest stack
        if arr[i] > tallest_stack:
            tallest_stack = arr[i]
    # If all the stacks are sorted correctly, return "YES"
    return "YES"

