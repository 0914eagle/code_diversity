def fib(n: int):
    
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)

