
def is_prime(num: int) -> bool:
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def prime_fib(n: int) -> int:
    if n == 1:
        return 2
    if n == 2:
        return 3
    prime_gen = generate_primes()
    fib_gen = generate_fibonacci()
    count = 0
    while count < n:
        num = next(fib_gen)
        if is_prime(num):
            count += 1
    return num

if __name__ == "__main__":
    n = int(input())
    print(prime_fib(n))
