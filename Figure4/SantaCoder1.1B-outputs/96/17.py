def count_up_to(n):
    
    primes = [2]
    for i in range(3, n + 1, 2):
        if i not in primes:
            primes.append(i)
    return primes


