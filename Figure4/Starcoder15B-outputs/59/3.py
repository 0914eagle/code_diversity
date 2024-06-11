def largest_prime_factor(n: int):
    
    largest_factor = 1
    factor = 2
    while factor <= n:
        if n % factor == 0:
            largest_factor = factor
            n //= factor
        else:
            factor += 1
    return largest_factor

if