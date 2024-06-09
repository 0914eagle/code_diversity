
def max_sum(arr):
    # Calculate the sum of the array
    sum = sum(arr)
    # Find the maximum element in the array
    max_element = max(arr)
    # Calculate the sum of the array after changing the sign of the maximum element
    sum_with_max_negative = sum - max_element
    # Return the maximum of the two sums
    return max(sum, sum_with_max_negative)

