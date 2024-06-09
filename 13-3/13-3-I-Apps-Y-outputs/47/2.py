
def solve(a):
    # Initialize the sum of non-deleted elements
    sum_non_deleted = 0
    # Initialize the number of elements left in the array
    n = len(a)
    # Initialize the parity of the last deleted element
    parity = 0
    # Iterate through the array
    for i in range(n):
        # If the current element has the opposite parity of the last deleted element
        if a[i] % 2 != parity:
            # Add the current element to the sum of non-deleted elements
            sum_non_deleted += a[i]
            # Delete the current element from the array
            a.pop(i)
            # Update the number of elements left in the array
            n -= 1
            # Update the parity of the last deleted element
            parity = 1 - parity
            # Break out of the loop
            break
    # If all elements have been deleted, return the sum of non-deleted elements
    return sum_non_deleted

