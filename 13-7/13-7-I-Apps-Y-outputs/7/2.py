
def polycarp_game(a):
    n = len(a)
    if n == 1:
        return a[0]
    
    # Initialize the sum of non-deleted elements
    sum_non_deleted = sum(a)
    
    # Initialize the parity of the last deleted element
    parity = 0
    
    # Iterate through the elements of the array
    for i in range(n):
        # If the current element has the opposite parity of the last deleted element, delete it
        if a[i] % 2 != parity:
            sum_non_deleted -= a[i]
            parity = 1 - parity
        # If the current element has the same parity as the last deleted element, do not delete it
        else:
            pass
    
    # Return the minimum possible sum of non-deleted elements
    return sum_non_deleted

