
def get_maximum_sum(a, b, k):
    # Sort the arrays a and b in non-decreasing order
    a.sort()
    b.sort()
    # Initialize the maximum sum to 0
    max_sum = 0
    # Loop through the arrays a and b and find the maximum sum
    for i in range(len(a)):
        for j in range(len(b)):
            # Check if the current sum is greater than the maximum sum
            if a[i] + b[j] > max_sum:
                # Update the maximum sum
                max_sum = a[i] + b[j]
    # Return the maximum sum
    return max_sum

