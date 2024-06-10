
def modp(n: int, p: int) -> int:
    result = 1
    base = 2 % p
    while n > 0:
        if n % 2 == 1:
            result = (result * base) % p
        base = (base * base) % p
        n //= 2
    return result
