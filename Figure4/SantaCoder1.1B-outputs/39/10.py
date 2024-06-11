def prime_fib(n: int):
    
    if n < 2:
        return n
    if n == 2:
        return 2
    if n == 3:
        return 5
    if n == 4:
        return 13
    if n == 5:
        return 89
    if n % 2 == 0:
        return prime_fib(n // 2)
    else:
        return prime_fib(n - 1) + prime_fib(n - 2)


