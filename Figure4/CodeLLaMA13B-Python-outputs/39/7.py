def prime_fib(n: int):
    
    a, b, i = 0, 1, 1
    while i < n:
        a, b = b, a + b
        if is_prime(b):
            i += 1
    return b


