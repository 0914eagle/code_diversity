
from itertools import combinations
from sympy import primerange

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_multiply_prime(a: int) -> bool:
    primes = list(primerange(2, 100))
    for comb in combinations(primes, 3):
        if comb[0] * comb[1] * comb[2] == a:
            return True
    return False

a = int(input())
print(is_multiply_prime(a))
