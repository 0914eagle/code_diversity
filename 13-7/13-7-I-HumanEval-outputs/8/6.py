
def fib4(n: int) -> int:
    
    if n < 0:
        raise ValueError("n must be non-negative")
    if n <= 3:
        return 0
    else:
        fib4_list = [0, 0, 2, 0]
        for i in range(4, n+1):
            fib4_list.append(fib4_list[i-1] + fib4_list[i-2] + fib4_list[i-3] + fib4_list[i-4])
        return fib4_list[n]

