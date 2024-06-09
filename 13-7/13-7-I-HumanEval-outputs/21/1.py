
def prime_fib(n: int) -> int:
    
    if n <= 0:
        raise ValueError("n must be greater than 0")

    fib_seq = [0, 1]
    i = 2
    while i <= n:
        fib_seq.append(fib_seq[i - 1] + fib_seq[i - 2])
        i += 1

    for num in fib_seq:
        if is_prime(num):
            if fib_seq.index(num) == n:
                return num

    return None

def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

