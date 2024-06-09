
def get_maximum_sum(a, b, k):
    # Sort both arrays in non-decreasing order
    a.sort()
    b.sort()
    # Initialize the maximum sum and the number of swaps used
    max_sum = 0
    swaps_used = 0
    # Loop through both arrays and find the maximum sum
    for i in range(len(a)):
        for j in range(len(b)):
            # Check if the sum of the elements at index i in both arrays is greater than the current maximum sum
            if a[i] + b[j] > max_sum:
                # Check if the number of swaps used is less than or equal to k
                if swaps_used <= k:
                    # Update the maximum sum and the number of swaps used
                    max_sum = a[i] + b[j]
                    swaps_used += 1
    # Return the maximum sum
    return max_sum

