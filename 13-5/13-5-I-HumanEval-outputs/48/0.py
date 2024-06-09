
def prime_fib(n: int) -> int:
    
    if n <= 0:
        raise ValueError("n must be a positive integer")

    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])

    for i in range(2, n):
        if is_prime(fib[i]):
            return fib[i]

    return -1

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

