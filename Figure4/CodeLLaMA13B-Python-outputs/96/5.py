def count_up_to(n):
    
    primes = []
    for i in range(2, n):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes


