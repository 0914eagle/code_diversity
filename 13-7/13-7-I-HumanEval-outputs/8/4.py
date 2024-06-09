
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
    previous = [0, 0, 2, 0]
    for i in range(4, n+1):
        previous.append(previous[i-1] + previous[i-2] + previous[i-3] + previous[i-4])
    return previous[n]

