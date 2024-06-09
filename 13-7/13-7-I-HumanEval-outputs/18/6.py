
def largest_prime_factor(n: int) -> int:
    
    if n < 2 or is_prime(n):
        return n
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

