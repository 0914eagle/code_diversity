
from itertools import combinations
from sympy import isprime

def generate_primes(limit):
    primes = []
    for num in range(2, limit):
        if isprime(num):
            primes.append(num)
    return primes

def is_multiply_prime(a: int) -> bool:
    primes = generate_primes(100)
    for combo in combinations(primes, 3):
        if combo[0] * combo[1] * combo[2] == a:
            return True
    return False

a = int(input())
print(is_multiply_prime(a))
