
def fib4(n: int) -> int:
    
    if n < 4:
        return 0
    else:
        fib_list = [0, 0, 2, 0]
        for i in range(4, n+1):
            fib_list.append(fib_list[i-1] + fib_list[i-2] + fib_list[i-3] + fib_list[i-4])
        return fib_list[n]

