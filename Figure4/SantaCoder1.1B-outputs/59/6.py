def largest_prime_factor(n: int):
    
    if n < 2:
        return n
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return i
    return n


