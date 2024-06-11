def largest_prime_factor(n: int):
    
    if n == 2:
        return 2
    if n % 2 == 0:
        return largest_prime_factor(n // 2)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return largest_prime_factor(n // i)
    return n


if