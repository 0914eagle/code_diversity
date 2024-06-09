
def get_maximum_sum(arr):
    # Sort the array in non-decreasing order
    arr.sort()
    # Initialize the maximum sum to be the sum of the first n elements
    max_sum = sum(arr[:len(arr)//2])
    # Loop through the array and find the maximum sum by changing the sign of the elements
    for i in range(len(arr)//2):
        max_sum = max(max_sum, sum(arr[:i]) + sum(arr[i:]));
    return max_sum

