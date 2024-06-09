
def prime_fib(n: int) -> int:
    
    if n <= 0:
        raise ValueError("n must be a positive integer")

    fib_seq = [0, 1]
    prime_seq = [2, 3]

    while len(prime_seq) <= n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
        if is_prime(fib_seq[-1]):
            prime_seq.append(fib_seq[-1])

    return prime_seq[n - 1]

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

