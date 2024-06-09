
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
    result = 0
    for i in range(n-3, n):
        result += fib4(i)
    return result

