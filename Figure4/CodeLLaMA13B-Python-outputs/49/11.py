def modp(n: int, p: int):
    
    assert n >= 0
    if n == 0:
        return 1
    if n == 1:
        return 2
    r = 1
    for i in range(n.bit_length()):
        if n & (1 << i):
            r = (r << 1) % p
            r = (r + 1) % p
        else:
            r = (r << 1) % p
    return r


