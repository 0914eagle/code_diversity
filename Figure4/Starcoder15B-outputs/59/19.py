def largest_prime_factor(n: int):
    
    if n < 2:
        raise ValueError('n must be greater than 1')
    if is_prime(n):
        return n
    for i in range(2, n):
        if n % i == 0:
            return largest_prime_factor(n // i)


