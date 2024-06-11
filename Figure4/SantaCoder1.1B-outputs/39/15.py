def prime_fib(n: int):
    
    if n <= 1:
        return n
    if n == 2:
        return 2
    if n % 2 == 0:
        return prime_fib(n // 2)
    else:
        return prime_fib(n - 1) + prime_fib(n - 2)


