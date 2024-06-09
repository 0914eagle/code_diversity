
def spaghetti_sort(arr):
    # First, sort the array in descending order
    arr.sort(reverse=True)
    # Initialize a variable to keep track of the height of the tallest stack
    tallest_stack = 0
    # Loop through the array and check if the stacks are sliding
    for i in range(len(arr) - 1):
        if arr[i] - arr[i+1] >= 2:
            # If the stacks are sliding, return "NO"
            return "NO"
        # Update the tallest stack height
        tallest_stack = max(tallest_stack, arr[i])
    # If the stacks are not sliding, return "YES"
    return "YES"

