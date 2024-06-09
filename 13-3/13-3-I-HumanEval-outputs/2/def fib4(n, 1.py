
def fib4(n: int) -> int:
    
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 2
    if n == 3:
        return 0
    fib4_seq = [0, 0, 2, 0]
    for i in range(4, n+1):
        fib4_seq.append(fib4_seq[i-1] + fib4_seq[i-2] + fib4_seq[i-3] + fib4_seq[i-4])
    return fib4_seq[n]

