
def get_maximum_sum(arr):
    # Sort the array in non-decreasing order
    arr.sort()
    # Initialize the maximum sum and number of elements to be changed
    max_sum = 0
    num_elements = len(arr) // 2
    # Loop through the array and calculate the maximum sum
    for i in range(num_elements):
        max_sum += arr[i] + arr[~i]
    return max_sum

