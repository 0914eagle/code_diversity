
def solve(a):
    n = len(a)
    if n == 1:
        return a[0]
    
    # Initialize the sum of non-deleted elements
    sum_non_deleted = sum(a)
    
    # Initialize the parity of the last deleted element as even
    parity = "even"
    
    for i in range(n-1):
        # If the current element has the opposite parity of the last deleted element, delete it
        if a[i] % 2 != parity:
            sum_non_deleted -= a[i]
            parity = "even" if parity == "odd" else "odd"
        # If the current element has the same parity as the last deleted element, skip it
        else:
            continue
    
    # If all elements have been deleted, the sum of non-deleted elements is zero
    if sum_non_deleted == 0:
        return 0
    # Otherwise, return the sum of non-deleted elements
    else:
        return sum_non_deleted

