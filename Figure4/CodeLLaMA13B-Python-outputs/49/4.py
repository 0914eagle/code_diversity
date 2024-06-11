def modp(n: int, p: int):
    
    if n == 0:
        return 1
    if n == 1:
        return 2
    if n % 2 == 0:
        return modp(n // 2, p) ** 2 % p
    return (modp(n // 2, p) ** 2 * 2) % p

