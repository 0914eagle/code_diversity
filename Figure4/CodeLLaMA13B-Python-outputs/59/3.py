def largest_prime_factor(n: int):
    
    # Hint: start with i = 2, and use the algorithm from Q3.
    i = 2
    while i * i <= n:
        if n % i == 0:
            n //= i
        else:
            i += 1
    return n


if