
def fib4(n: int) -> int:
    
    if n <= 3:
        return n
    else:
        fib_n_minus_4 = fib4(n-4)
        fib_n_minus_3 = fib4(n-3)
        fib_n_minus_2 = fib4(n-2)
        fib_n_minus_1 = fib4(n-1)
        return fib_n_minus_4 + fib_n_minus_3 + fib_n_minus_2 + fib_n_minus_1

