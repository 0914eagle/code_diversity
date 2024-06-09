
def solve(a):
    n = len(a)
    if n == 1:
        return a[0]
    
    # initialize the sum of non-deleted elements
    sum_non_deleted = sum(a)
    
    # initialize the parity of the last deleted element
    parity = 0
    
    for i in range(n-1):
        # find the index of the element with the opposite parity
        if parity == 0:
            index = next((i for i, x in enumerate(a[i+1:]) if x % 2 == 1), None)
        else:
            index = next((i for i, x in enumerate(a[i+1:]) if x % 2 == 0), None)
        
        # if such an element exists, delete it and update the parity
        if index is not None:
            sum_non_deleted -= a[i+1+index]
            parity = 1 - parity
        else:
            break
    
    return sum_non_deleted

