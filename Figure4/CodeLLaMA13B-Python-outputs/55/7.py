def fib(n: int):
    
    if n <= 0:
        raise ValueError("n must be >= 1")
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


if