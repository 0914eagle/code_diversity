
def largest_prime_factor(n: int) -> int:
    
    if n < 2 or n % 2 == 0:
        return 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return i
        i += 2
    return n

