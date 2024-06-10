
import math

def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def prime_length(string: str) -> bool:
    return is_prime(len(string))

if __name__ == "__main__":
    string = input().strip()
    print(prime_length(string))
