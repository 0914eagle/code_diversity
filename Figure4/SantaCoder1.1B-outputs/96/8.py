def count_up_to(n):
    
    primes = [2]
    for i in range(3, n + 1):
        if i not in primes:
            primes.append(i)
            for j in range(2, i):
                if i % j == 0:
                    primes.append(i)
                    break
    return primes


