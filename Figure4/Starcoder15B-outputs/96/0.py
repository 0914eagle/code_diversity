def count_up_to(n):
    
    # your code here
    if n == 0:
        return []
    else:
        primes = []
        for i in range(2, n):
            if is_prime(i):
                primes.append(i)
        return primes

