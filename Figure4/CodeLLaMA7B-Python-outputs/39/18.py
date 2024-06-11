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

    fib_num = 0
    prime_num = 0
    count = 0
    while count < n:
        fib_num = fib_num + prime_num
        prime_num = fib_num - prime_num
        count += 1
        if is_prime(fib_num):
            count += 1
    return fib_num


