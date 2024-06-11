def prime_fib(n: int):
    
    if n < 2:
        return n
    elif n == 2:
        return 2
    else:
        return prime_fib(n - 1) + prime_fib(n - 2)


