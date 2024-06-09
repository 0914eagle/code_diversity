
def get_maximum_sum(arr):
    # Sort the array in non-decreasing order
    arr.sort()
    # Initialize the sum to 0
    sum = 0
    # Loop through the array and find the maximum sum
    for i in range(len(arr)):
        # If the current element is positive, add it to the sum
        if arr[i] > 0:
            sum += arr[i]
        # If the current element is negative, subtract it from the sum
        else:
            sum -= arr[i]
    # Return the maximum sum
    return sum

