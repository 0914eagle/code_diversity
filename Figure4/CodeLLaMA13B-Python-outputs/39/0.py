def prime_fib(n: int):
    
    if n <= 0:
        raise ValueError("n must be greater than 0")
    fib_list = [1, 1]
    fib_num = 1
    while True:
        fib_num = fib_list[-1] + fib_list[-2]
        fib_list.append(fib_num)
        if is_prime(fib_num) and is_fib(fib_num):
            if n == 1:
                return fib_num
            else:
                n -= 1


