def prime_fib(n: int):
    
    a, b = 0, 1
    while True:
        if is_prime(b) and is_fib(b):
            if n == 1:
                return b
            n -= 1
        a, b = b, a + b


