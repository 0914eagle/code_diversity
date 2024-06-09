
def solve(a):
    n = len(a)
    if n == 1:
        return a[0]
    
    # initialize the sum of non-deleted elements
    sum_non_deleted = sum(a)
    
    # initialize the parity of the last deleted element
    parity = 0
    
    for i in range(n):
        # if it is the first move, choose any element and delete it
        if i == 0:
            parity = a[i] % 2
            sum_non_deleted -= a[i]
            continue
        
        # if it is the second or any next move:
        # if the last deleted element was odd, choose any even element and delete it
        # if the last deleted element was even, choose any odd element and delete it
        if parity == 0:
            for j in range(i, n):
                if a[j] % 2 == 0:
                    parity = a[j] % 2
                    sum_non_deleted -= a[j]
                    break
        else:
            for j in range(i, n):
                if a[j] % 2 == 1:
                    parity = a[j] % 2
                    sum_non_deleted -= a[j]
                    break
    
    return sum_non_deleted

