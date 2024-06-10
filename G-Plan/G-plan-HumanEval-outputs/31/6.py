
from itertools import combinations
from sympy import isprime

def get_primes(limit):
    return [num for num in range(2, limit) if isprime(num)]

def is_multiply_prime(a: int) -> bool:
    primes = get_primes(100)
    for prime_combination in combinations(primes, 3):
        if prime_combination[0] * prime_combination[1] * prime_combination[2] == a:
            return True
    return False

a = int(input())
print(is_multiply_prime(a))
