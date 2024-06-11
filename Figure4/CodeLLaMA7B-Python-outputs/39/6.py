def prime_fib(n: int):
    
    if n == 1:
        return 2
    elif n == 2:
        return 3
    elif n == 3:
        return 5
    else:
        fib_list = [2, 3, 5]
        for i in range(4, n + 1):
            fib_list.append(fib_list[i - 1] + fib_list[i - 2])
            if is_prime(fib_list[i]):
                return fib_list[i]


