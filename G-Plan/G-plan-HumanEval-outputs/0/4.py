
import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def largest_prime_factor(n: int) -> int:
    largest_prime = 0
    while n % 2 == 0:
        largest_prime = 2
        n //= 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            largest_prime = i
            n //= i
    if n > 2:
        largest_prime = n
    return largest_prime

if __name__ == "__main__":
    n = int(input())
    print(largest_prime_factor(n))
