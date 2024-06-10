
import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def largest_prime_factor(n: int) -> int:
    def is_factor(num, factor):
        return num % factor == 0

    def get_factors(num):
        factors = set()
        for i in range(2, int(math.sqrt(num)) + 1):
            if is_factor(num, i):
                factors.add(i)
                factors.add(num // i)
        return factors

    factors = get_factors(n)
    prime_factors = [factor for factor in factors if is_prime(factor)]
    return max(prime_factors)

if __name__ == "__main__":
    n = int(input())
    print(largest_prime_factor(n))
