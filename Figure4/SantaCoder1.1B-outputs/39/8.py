def prime_fib(n: int):
    
    if n < 2:
        return 0
    if n == 2:
        return 1
    if n % 2 == 0:
        return 0
    if n % 3 == 0:
        return 0
    if n % 5 == 0:
        return 0
    i = 0
    j = 1
    while j < n:
        if n % j == 0:
            i += 1
            j += 1
        else:
            j += 1
    return i


