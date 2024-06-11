def prime_fib(n: int):
    
    if n <= 0:
        raise ValueError("n must be greater than 0")
    fib_nums = [1, 1]
    prime_fibs = [2, 3]
    while len(prime_fibs) < n:
        fib_nums.append(fib_nums[-1] + fib_nums[-2])
        if is_prime(fib_nums[-1]):
            prime_fibs.append(fib_nums[-1])
    return prime_fibs[n - 1]


