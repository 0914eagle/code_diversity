def prime_fib(n: int):
    
    if n == 1:
        return 2
    if n == 2:
        return 3
    if n == 3:
        return 5

    a, b = 2, 3
    for _ in range(3, n):
        a, b = b, a + b

    return b


if __name__ == "__main__":
    from doctest import testmod

    testmod()
