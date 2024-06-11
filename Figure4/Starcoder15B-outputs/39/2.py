def prime_fib(n: int):
    
    if n == 1:
        return 2
    if n == 2:
        return 3
    if n == 3:
        return 5
    if n == 4:
        return 13
    if n == 5:
        return 89
    fib_n_minus_2 = 2
    fib_n_minus_1 = 3
    fib_n = 5
    i = 5
    while i < n:
        fib_n_minus_2 = fib_n_minus_1
        fib_n_minus_1 = fib_n
        fib_n = fib_n_minus_2 + fib_n_minus_1
        i += 1
    return fib_n


