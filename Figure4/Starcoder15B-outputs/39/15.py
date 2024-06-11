def prime_fib(n: int):
    
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        fib_n_minus_2 = 2
        fib_n_minus_1 = 3
        fib_n = 5
        i = 3
        while i < n:
            fib_n_minus_2 = fib_n_minus_1
            fib_n_minus_1 = fib_n
            fib_n = fib_n_minus_2 + fib_n_minus_1
            i += 1
        return fib_n


if __name__ == "__main__":
    import