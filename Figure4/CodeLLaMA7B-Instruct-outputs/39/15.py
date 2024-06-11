


def prime_fib(n: int):
    
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
        if is_prime(a) and a > 1:
            return a
    return -1

def
