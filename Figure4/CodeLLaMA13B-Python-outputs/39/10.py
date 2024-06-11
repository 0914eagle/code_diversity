def prime_fib(n: int):
    
    a, b = 0, 1
    count = 0
    while True:
        a, b = b, a + b
        count += 1
        if is_prime(b) and is_fib(b):
            if count == n:
                return b


