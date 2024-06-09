
def solve(arr):
    n = len(arr)
    if n == 1:
        return 0
    # Sort the array
    arr.sort()
    # Initialize the minimum size of the subsegment to remove
    min_size = 0
    # Iterate through the array
    for i in range(n-1):
        # If the current element is equal to the next element, increase the minimum size of the subsegment to remove
        if arr[i] == arr[i+1]:
            min_size += 1
        # If the current element is not equal to the next element, check if the minimum size of the subsegment to remove is greater than 1
        elif min_size > 1:
            # If the minimum size of the subsegment to remove is greater than 1, return the minimum size
            return min_size
            # Otherwise, set the minimum size of the subsegment to remove to 0
    return min_size

