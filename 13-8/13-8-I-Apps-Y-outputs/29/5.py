
def solve(a, b, k):
    # Sort the arrays a and b in non-decreasing order
    a.sort()
    b.sort()
    # Initialize the maximum sum to 0
    max_sum = 0
    # Loop through each element in a and b
    for i in range(len(a)):
        # Check if the current element in a is less than or equal to the current element in b
        if a[i] <= b[i]:
            # Add the current element in a to the maximum sum
            max_sum += a[i]
        # If the current element in a is greater than the current element in b
        else:
            # Check if we have remaining moves
            if k > 0:
                # Decrement the number of remaining moves
                k -= 1
                # Swap the current element in a with the current element in b
                a[i], b[i] = b[i], a[i]
                # Add the current element in a to the maximum sum
                max_sum += a[i]
            # If we have no remaining moves, return the maximum sum
            else:
                return max_sum
    # Return the maximum sum
    return max_sum

