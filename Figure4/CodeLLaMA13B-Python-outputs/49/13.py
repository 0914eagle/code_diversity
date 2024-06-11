def modp(n: int, p: int):
    
    assert n >= 0
    assert p > 1
    if n == 0:
        return 1
    if n == 1:
        return 2
    m = modp(n // 2, p)
    m2 = (m * m) % p
    if n % 2 == 0:
        return m2
    else:
        return (m2 * 2) % p


