def prime_fib(n: int):
    
    if n <= 0:
        raise ValueError("n must be greater than 0")
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return a


if __name__ == "__main__":
    import doctest

    doctest.testmod()
