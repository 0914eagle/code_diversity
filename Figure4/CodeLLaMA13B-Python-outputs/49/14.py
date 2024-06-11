def modp(n: int, p: int):
    
    assert n >= 0
    if n == 0:
        return 1
    return (modp(n // 2, p) ** 2) % p * (2 + (n % 2) - 1) % p + 1


