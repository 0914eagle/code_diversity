def count_up_to(n):
    
    primes = []
    for i in range(2, n):
        if is_prime(i):
            primes.append(i)
        if len(primes) == n:
            break
    return primes


