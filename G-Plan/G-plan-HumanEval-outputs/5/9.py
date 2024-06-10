
import math

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_length(string: str) -> bool:
    length = len(string)
    return is_prime(length)

# Test the function with the provided examples
print(prime_length('Hello'))
print(prime_length('abcdcba'))
print(prime_length('kittens'))
print(prime_length('orange'))
