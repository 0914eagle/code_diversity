
def fib4(n: int) -> int:
    
    if n <= 3:
        return 0
    else:
        fib4_n_1 = 0
        fib4_n_2 = 0
        fib4_n_3 = 2
        fib4_n_4 = 0
        for i in range(4, n+1):
            fib4_n = fib4_n_1 + fib4_n_2 + fib4_n_3 + fib4_n_4
            fib4_n_1 = fib4_n_2
            fib4_n_2 = fib4_n_3
            fib4_n_3 = fib4_n_4
            fib4_n_4 = fib4_n
        return fib4_n

