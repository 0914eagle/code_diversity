def prime_fib(n: int):
    
    fib_nums = [1, 1]
    for _ in range(n - 1):
        fib_nums.append(fib_nums[-1] + fib_nums[-2])
    return fib_nums[-1]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
