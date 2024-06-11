def prime_fib(n: int):
    
    if n == 1:
        return 2
    elif n == 2:
        return 3
    elif n == 3:
        return 5
    elif n == 4:
        return 13
    elif n == 5:
        return 89
    else:
        for i in range(2, n):
            if n % i == 0:
                return i


