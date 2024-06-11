def largest_prime_factor(n: int):
    
    if is_prime(n):
        return n
    for i in range(2, n):
        if n % i == 0:
            return largest_prime_factor(n // i)


