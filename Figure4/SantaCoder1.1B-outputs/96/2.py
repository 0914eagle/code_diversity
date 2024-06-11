def count_up_to(n):
    
    primes = [2, 3]
    for i in range(4, n + 1):
        if i not in primes:
            primes.append(i)
    return primes


