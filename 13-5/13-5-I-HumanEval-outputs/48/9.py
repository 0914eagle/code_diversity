
def prime_fib(n: int) -> int:
    
    if n <= 0:
        raise ValueError("n must be a positive integer")

    fib = [0, 1]
    i = 2
    while i <= n:
        fib.append(fib[i-1] + fib[i-2])
        i += 1

    for num in fib[n:]:
        if is_prime(num):
            return num

    return None

def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

