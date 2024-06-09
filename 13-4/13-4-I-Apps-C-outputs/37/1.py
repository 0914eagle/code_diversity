
def find_polynomial(p, k):
    if p >= k:
        return -1
    
    d = 1
    while p % k != 0:
        p *= k
        d += 1
    
    a = [0] * d
    a[d-1] = 1
    return d, a

