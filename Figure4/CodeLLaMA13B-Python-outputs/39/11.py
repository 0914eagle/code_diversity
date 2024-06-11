def prime_fib(n: int):
    
    a, b = 0, 1
    while True:
        if is_prime(b):
            n -= 1
            if n == 0:
                return b
        a, b = b, a + b


