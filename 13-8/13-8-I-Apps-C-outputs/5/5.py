
def solve(arr):
    n = len(arr)
    if n == 1:
        return 0
    # Sort the array
    arr.sort()
    # Initialize variables for the minimum size of the subsegment to remove
    min_size = 0
    # Iterate over the array
    for i in range(n-1):
        # If the current element is the same as the next element
        if arr[i] == arr[i+1]:
            # Update the minimum size of the subsegment to remove
            min_size = max(min_size, 2)
        # If the current element is not the same as the next element and the next element is not the same as the element after that
        elif arr[i+1] != arr[i+2]:
            # Update the minimum size of the subsegment to remove
            min_size = max(min_size, 1)
    return min_size

