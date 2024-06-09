
def get_maximum_sum(a, b, k):
    # Sort both arrays in non-decreasing order
    a.sort()
    b.sort()
    # Initialize the maximum sum and the current sum
    max_sum = 0
    current_sum = 0
    # Loop through both arrays and calculate the current sum
    for i in range(len(a)):
        current_sum += a[i]
        current_sum += b[i]
        # If the current sum is greater than the maximum sum, update the maximum sum
        if current_sum > max_sum:
            max_sum = current_sum
        # If the number of swaps used is greater than k, break the loop
        if i >= k:
            break
    return max_sum

