
import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def largest_prime_factor(n: int) -> int:
    def get_factors(num):
        factors = []
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                factors.append(i)
                factors.append(num // i)
        return factors

    factors = get_factors(n)
    prime_factors = [factor for factor in factors if is_prime(factor)]
    return max(prime_factors)

if __name__ == "__main__":
    n = int(input().strip())
    print(largest_prime_factor(n))
