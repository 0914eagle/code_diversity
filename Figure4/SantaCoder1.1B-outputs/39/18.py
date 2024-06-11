def prime_fib(n: int):
    
    if n < 2:
        return 0
    elif n == 2:
        return 1
    elif n % 2 == 0:
        return prime_fib(n // 2)
    else:
        return prime_fib(n - 1) + prime_fib(n - 2)


