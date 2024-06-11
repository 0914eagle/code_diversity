def largest_prime_factor(n: int):
    
    prime_factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            prime_factors.append(i)
    if n > 1:
        prime_factors.append(n)
    return prime_factors[-1]


if