def largest_prime_factor(n: int):
    
    if is_prime(n):
        return n
    for i in range(n, 1, -1):
        if n % i == 0 and is_prime(i):
            return i


