
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
            index = find_even(a)
        else:
            index = find_odd(a)
        
        # if such an element exists, delete it and update the sum of non-deleted elements
        if index != -1:
            sum_non_deleted -= a[index]
            a.pop(index)
        else:
            break
        
        # update the parity of the last deleted element
        parity = 1 - parity
    
    return sum_non_deleted

def find_even(a):
    for i in range(len(a)):
        if a[i] % 2 == 0:
            return i
    return -1

def find_odd(a):
    for i in range(len(a)):
        if a[i] % 2 == 1:
            return i
    return -1

