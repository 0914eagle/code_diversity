
def solve(a):
    n = len(a)
    if n == 1:
        return a[0]
    
    # initialize the sum of non-deleted elements
    sum_non_deleted = sum(a)
    
    # initialize the parity of the last deleted element as even
    parity = "even"
    
    for i in range(n-1):
        # find the index of the element with the opposite parity
        if parity == "even":
            index = find_even_index(a)
        else:
            index = find_odd_index(a)
        
        # if such an element exists, delete it and update the parity
        if index != -1:
            sum_non_deleted -= a[index]
            parity = "even" if parity == "odd" else "odd"
        else:
            break
    
    return sum_non_deleted

def find_even_index(a):
    for i in range(len(a)):
        if a[i] % 2 == 0:
            return i
    return -1

def find_odd_index(a):
    for i in range(len(a)):
        if a[i] % 2 == 1:
            return i
    return -1

