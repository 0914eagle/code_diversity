
def get_minimum_moves(a, k):
    n = len(a)
    x = 0
    moves = 0
    while True:
        # increment x by 1
        x += 1
        moves += 1
        
        # check if all elements of a are divisible by k
        if all(a[i] % k == 0 for i in range(n)):
            break
        
        # find the first element that is not divisible by k
        i = 0
        while i < n and a[i] % k == 0:
            i += 1
        
        # if there is no such element, we can't make the array divisible by k
        if i == n:
            return -1
        
        # add x to the element at index i and increment x by 1
        a[i] += x
    
    return moves

