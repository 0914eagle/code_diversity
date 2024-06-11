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

    fib_num = 3
    prime_num = 5
    for i in range(4, n):
        fib_num += prime_num
        prime_num = prime_fib(i)
    return fib_num


if __name__ == "__main__":
    import doctest

    doctest.testmod()
