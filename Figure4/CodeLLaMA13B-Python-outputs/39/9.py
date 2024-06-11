def prime_fib(n: int):
    
    if n <= 0:
        raise ValueError("n should be greater than 0")
    fib = [0, 1]
    prime = [2]
    while len(prime) < n:
        fib.append(fib[-1] + fib[-2])
        if is_prime(fib[-1]):
            prime.append(fib[-1])
    return prime[n - 1]


