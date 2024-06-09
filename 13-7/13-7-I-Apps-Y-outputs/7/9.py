
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
        
        # if it is the second or any next move, choose any element with the only restriction: its parity should differ from the parity of the element deleted on the previous move
        else:
            if parity == 0:
                # if the last deleted element was even, choose any odd element and delete it
                for j in range(i, n):
                    if a[j] % 2 == 1:
                        parity = 1
                        sum_non_deleted -= a[j]
                        break
            else:
                # if the last deleted element was odd, choose any even element and delete it
                for j in range(i, n):
                    if a[j] % 2 == 0:
                        parity = 0
                        sum_non_deleted -= a[j]
                        break
        
        # if after some move Polycarp cannot make a move, the game ends
        if i == n-1 and parity == a[i] % 2:
            break
    
    return sum_non_deleted

