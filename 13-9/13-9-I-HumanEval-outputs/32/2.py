
def fib4(n: int) -> int:
    
    if n < 4:
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

