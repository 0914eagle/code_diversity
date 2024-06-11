def count_up_to(n):
    
    if n < 2:
        return []
    primes = [2]
    for i in range(3, n):
        if is_prime(i):
            primes.append(i)
    return primes


