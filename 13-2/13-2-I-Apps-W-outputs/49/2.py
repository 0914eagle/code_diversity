
def get_maximum_median(arr, k):
    # Sort the array in non-decreasing order
    arr.sort()
    # Initialize the median and the number of operations made
    median = arr[len(arr) // 2]
    operations = 0
    # Loop through the array and check if the median can be increased
    for i in range(len(arr)):
        if arr[i] < median and operations < k:
            arr[i] += 1
            operations += 1
    # Return the maximum possible median after the operations
    return median

