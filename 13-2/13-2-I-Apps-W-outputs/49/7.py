
def get_maximum_median(arr, k):
    # Sort the array in non-decreasing order
    arr.sort()
    # Initialize the median and the number of operations made
    median = arr[len(arr) // 2]
    operations = 0
    # Loop through the array and find the element that is closest to the median
    for i in range(len(arr)):
        if abs(arr[i] - median) < abs(arr[(i + 1) % len(arr)] - median):
            # If the element is not already the median, increase it by 1 and update the median
            if arr[i] != median:
                arr[i] += 1
                median += 1
                operations += 1
                # If the number of operations exceeds the given limit, break the loop
                if operations > k:
                    break
    # Return the maximum possible median
    return median

