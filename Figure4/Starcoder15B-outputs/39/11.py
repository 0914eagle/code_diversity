def prime_fib(n: int):
    
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        fib_list = [2, 3]
        while len(fib_list) < n:
            fib_list.append(fib_list[-1] + fib_list[-2])
        return next(x for x in fib_list if is_prime(x))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
/python/problem_0001.py



