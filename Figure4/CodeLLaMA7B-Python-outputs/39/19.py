def prime_fib(n: int):
    
    if n == 1:
        return 2
    if n == 2:
        return 3
    if n == 3:
        return 5

    fib_num = 1
    prime_num = 2
    count = 2
    while count < n:
        fib_num += prime_num
        if is_prime(fib_num):
            prime_num = fib_num
            count += 1
    return prime_num


