def count_up_to(n):
    
    # your code here
    if n < 2:
        return []
    primes = [2]
    for i in range(3, n, 2):
        if is_prime(i):
            primes.append(i)
    return primes


