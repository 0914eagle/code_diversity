
from math import isqrt

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def prime_length(string: str) -> bool:
    return is_prime(len(string))

# Test the function with examples
print(prime_length('Hello'))
print(prime_length('abcdcba'))
print(prime_length('kittens'))
print(prime_length('orange'))
