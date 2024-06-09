
def prime_fib(n: int) -> int:
    
    fib = [0, 1]
    i = 2
    while i <= n:
        fib.append(fib[i-1] + fib[i-2])
        i += 1
    for i in range(2, n+1):
        if is_prime(fib[i]):
            return fib[i]
    return -1

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

