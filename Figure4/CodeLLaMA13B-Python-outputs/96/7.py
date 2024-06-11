def count_up_to(n):
    
    if n <= 1:
        return []
    primes = [2]
    for i in range(3, n, 2):
        for j in primes:
            if j > int(i ** 0.5) + 1:
                primes.append(i)
                break
            if i % j == 0:
                break
    return primes


