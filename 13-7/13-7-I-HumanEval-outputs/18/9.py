
def largest_prime_factor(n: int) -> int:
    
    if n <= 1 or is_prime(n):
        return n

    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

def is_prime(n: int) -> bool:
    
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

