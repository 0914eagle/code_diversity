
def get_max_sum(a, b, k):
    # Sort both arrays in non-decreasing order
    a.sort()
    b.sort()
    # Initialize the maximum sum to 0
    max_sum = 0
    # Loop through each element in a and b
    for i in range(len(a)):
        # Check if the current element in a is less than or equal to the current element in b
        if a[i] <= b[i]:
            # If so, add the current element in a to the maximum sum
            max_sum += a[i]
        else:
            # If not, check if we have any swaps left
            if k > 0:
                # If we do, swap the current element in a with the current element in b and decrease the number of swaps by 1
                a[i], b[i] = b[i], a[i]
                k -= 1
                # Add the current element in a to the maximum sum
                max_sum += a[i]
            else:
                # If we don't, add the current element in b to the maximum sum
                max_sum += b[i]
    # Return the maximum sum
    return max_sum

