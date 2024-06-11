def fib(n: int):
    
    if n < 1:
        raise ValueError("n must be positive")
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


