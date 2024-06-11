def count_up_to(n):
    
    # Your code here
    if n <= 1:
        return []
    primes = []
    for i in range(2, n):
        if is_prime(i):
            primes.append(i)
    return primes


