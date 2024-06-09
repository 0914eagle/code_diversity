
def fib4(n: int) -> int:
    
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 2
    if n == 3:
        return 0
    fib_n_1 = 0
    fib_n_2 = 0
    fib_n_3 = 2
    fib_n_4 = 0
    for i in range(4, n+1):
        fib_n = fib_n_1 + fib_n_2 + fib_n_3 + fib_n_4
        fib_n_1 = fib_n_2
        fib_n_2 = fib_n_3
        fib_n_3 = fib_n_4
        fib_n_4 = fib_n
    return fib_n

