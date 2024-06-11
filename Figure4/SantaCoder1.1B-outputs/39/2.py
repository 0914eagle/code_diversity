def prime_fib(n: int):
    
    if n < 2:
        return n
    elif n == 2:
        return 2
    else:
        for i in range(3, n):
            if n % i == 0:
                return i
        return n


