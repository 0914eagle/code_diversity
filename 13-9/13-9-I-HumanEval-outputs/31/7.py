
def prime_fib(n: int) -> int:
    
    if n < 1:
        raise ValueError("n must be greater than or equal to 1")

    fib_seq = [0, 1]
    i = 2
    while i <= n:
        fib_seq.append(fib_seq[i - 1] + fib_seq[i - 2])
        i += 1

    for fib in fib_seq:
        if is_prime(fib):
            n -= 1
            if n == 0:
                return fib

    return None

def is_prime(num: int) -> bool:
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

