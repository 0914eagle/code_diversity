def modp(n: int, p: int):
    
    assert n >= 0 and p > 1
    if n == 0:
        return 1
    elif n == 1:
        return 2
    else:
        return (2 * modp(n - 1, p)) % p


