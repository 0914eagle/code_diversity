
from math import isqrt

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def prime_length(string: str) -> bool:
    length = len(string)
    return is_prime(length)

if __name__ == "__main__":
    input_string = input().strip()
    print(prime_length(input_string))
