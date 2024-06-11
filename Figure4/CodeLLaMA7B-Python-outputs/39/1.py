def prime_fib(n: int):
    
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        a, b = 2, 3
        for _ in range(n - 2):
            a, b = b, a + b
        return b


if __name__ == "__main__":
    from doctest import testmod

    testmod()