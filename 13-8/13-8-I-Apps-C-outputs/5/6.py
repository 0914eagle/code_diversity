
def solve(arr):
    n = len(arr)
    if n == 1:
        return 0

    # Sort the array
    arr.sort()

    # Initialize the minimum size of the subsegment to remove
    min_size = 0

    # Iterate over the array
    for i in range(n - 1):
        # Check if the current element is equal to the next element
        if arr[i] == arr[i + 1]:
            # If they are equal, we need to remove the subsegment starting from the current element
            # and ending at the next element
            min_size = max(min_size, 2)
        else:
            # If they are not equal, we need to remove the subsegment starting from the current element
            # and ending at the next element - 1
            min_size = max(min_size, 1)

    return min_size

