
def prime_fib(n: int) -> int:
    
    if n < 1:
        raise ValueError("n must be greater than or equal to 1")

    fib_seq = [0, 1]
    prime_seq = [2, 3]

    while len(prime_seq) < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
        if all(fib_seq[-1] % p != 0 for p in prime_seq):
            prime_seq.append(fib_seq[-1])

    return prime_seq[n - 1]

