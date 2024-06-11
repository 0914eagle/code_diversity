def count_up_to(n):
    
    if n <= 1:
        return []
    primes = [2]
    for i in range(3, n, 2):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                break
        else:
            primes.append(i)
    return primes
