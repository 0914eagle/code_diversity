def prime_fib(n: int):
    
    if n < 1:
        return None
    elif n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        fib = [2, 3]
        for i in range(2, n):
            fib.append(fib[i - 1] + fib[i - 2])
        for i in range(len(fib) - 1, 0, -1):
            if is_prime(fib[i]):
                return fib[i]


