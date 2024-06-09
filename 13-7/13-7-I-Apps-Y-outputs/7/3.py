
def solve(a):
    # Initialize the sum of non-deleted elements
    sum_non_deleted = 0
    # Initialize the number of elements in the array
    n = len(a)
    # Initialize the index of the last deleted element
    last_deleted = 0
    # Initialize the parity of the last deleted element
    parity = 0

    # Iterate through the array
    for i in range(n):
        # If the current element is even and the parity is odd, or the current element is odd and the parity is even
        if (a[i] % 2 == 0 and parity % 2 == 1) or (a[i] % 2 == 1 and parity % 2 == 0):
            # Update the sum of non-deleted elements
            sum_non_deleted += a[i]
            # Update the index of the last deleted element
            last_deleted = i
            # Update the parity of the last deleted element
            parity = a[i] % 2
        # If the current element is even and the parity is even, or the current element is odd and the parity is odd
        elif (a[i] % 2 == 0 and parity % 2 == 0) or (a[i] % 2 == 1 and parity % 2 == 1):
            # Do nothing
            pass
        # If the current element is even and the parity is odd, or the current element is odd and the parity is even
        else:
            # Update the sum of non-deleted elements
            sum_non_deleted += a[i]
            # Update the index of the last deleted element
            last_deleted = i
            # Update the parity of the last deleted element
            parity = a[i] % 2

    # Return the minimum possible sum of non-deleted elements
    return sum_non_deleted

