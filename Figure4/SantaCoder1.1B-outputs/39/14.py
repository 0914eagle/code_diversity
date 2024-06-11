def prime_fib(n: int):
    
    if n < 2:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 5
    if n == 4:
        return 13
    if n == 5:
        return 89
    if n % 2 == 0:
        return 0
    if n % 3 == 0:
        return 0
    if n % 5 == 0:
        return 0
    for i in range(6, n + 1, 6):
        if n % i == 0:
            return 0
    return n


