
def prime_fib(n: int) -> int:
    
    if n < 1:
        raise ValueError("n must be greater than or equal to 1")

    fib_seq = [0, 1]
    i = 2
    while len(fib_seq) <= n:
        fib_seq.append(fib_seq[i-1] + fib_seq[i-2])
        i += 1

    for i in range(2, n+1):
        if is_prime(fib_seq[i]):
            return fib_seq[i]

    return None

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

