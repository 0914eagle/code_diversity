def count_up_to(n):
    
    # TODO: Write your code here.
    primes = [True] * (n+1)
    primes[0] = False
    primes[1] = False
    for i in range(2, int(n**0.5)+1):
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = False
    return [i for i, p in enumerate(primes) if p]


