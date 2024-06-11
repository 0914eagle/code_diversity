def prime_fib(n: int):
    
    if n <= 0:
        raise ValueError("n must be greater than 0")

    fib = [1, 1]
    prime = [2, 3, 5, 7]
    i = 4
    while True:
        fib.append(fib[i - 1] + fib[i - 2])
        if is_prime(fib[i]):
            prime.append(fib[i])
            if len(prime) == n:
                return prime[n - 1]
        i += 1


