
def get_maximum_sum(a, b, k):
    # Sort the arrays a and b in non-decreasing order
    a.sort()
    b.sort()
    # Initialize the maximum sum to 0
    max_sum = 0
    # Loop through the arrays a and b and calculate the sum
    for i in range(len(a)):
        max_sum += a[i] + b[i]
    # Return the maximum sum
    return max_sum

