def prime_fib(n: int):
    
    if n < 1:
        raise ValueError("n must be a positive integer")
    if n == 1:
        return 2
    if n == 2:
        return 3
    fib_n_minus_1 = 2
    fib_n_minus_2 = 3
    fib_n = 0
    i = 3
    while i <= n:
        fib_n = fib_n_minus_1 + fib_n_minus_2
        if is_prime(fib_n):
            fib_n_minus_2 = fib_n_minus_1
            fib_n_minus_1 = fib_n
            i += 1
    return fib_n


if __name__ == "__main__":
    import doctest
    doctest.testmod()
/python/00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000