
def prime_fib(n: int) -> int:
    
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        if is_prime(b):
            return b
    return -1

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

