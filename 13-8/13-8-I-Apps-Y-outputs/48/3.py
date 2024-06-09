
def is_sorted_correctly(arr):
    # Sort the array in non-decreasing order
    arr.sort()
    # Initialize a variable to keep track of the current height
    current_height = 0
    # Iterate through the array and check if the height changes by 2 or more at any point
    for i in range(len(arr)):
        if arr[i] - current_height >= 2:
            return "NO"
        current_height = arr[i]
    return "YES"

