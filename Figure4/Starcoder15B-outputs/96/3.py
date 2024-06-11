def count_up_to(n):
    
    # your code here
    primes = []
    for i in range(2, n):
        if is_prime(i):
            primes.append(i)
    return primes

