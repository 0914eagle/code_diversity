def prime_fib(n: int):
    
    fib_list = [1, 1]
    while len(fib_list) < n:
        fib_list.append(fib_list[-1] + fib_list[-2])
    return next(filter(is_prime, fib_list))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
/python/exercism/python/pangram/pangram.py



