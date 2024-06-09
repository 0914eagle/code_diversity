
def get_polynomial(p, k):
    if p >= k:
        return -1
    
    d = 1
    a = [p]
    while a[-1] % k != 0:
        a.append(a[-1] // k)
        d += 1
    
    return d, a[:-1]

