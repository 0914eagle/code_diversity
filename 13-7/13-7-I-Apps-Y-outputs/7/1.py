
def solve(a):
    n = len(a)
    if n == 1:
        return a[0]
    
    # initialize the sum of non-deleted elements
    sum_non_deleted = sum(a)
    
    # initialize the parity of the last deleted element as odd
    parity = "odd"
    
    # iterate through the array
    for i in range(n):
        # if the current element has the opposite parity of the last deleted element
        if parity == "odd" and a[i] % 2 == 0:
            # delete the current element and update the parity
            parity = "even"
            sum_non_deleted -= a[i]
        elif parity == "even" and a[i] % 2 == 1:
            # delete the current element and update the parity
            parity = "odd"
            sum_non_deleted -= a[i]
    
    # return the minimum possible sum of non-deleted elements
    return sum_non_deleted

