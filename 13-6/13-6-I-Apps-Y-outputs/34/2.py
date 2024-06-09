
import math

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def count_divisors(n):
    divisors = 0
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            divisors += 2
    if int(math.sqrt(n))**2 == n:
        divisors -= 1
    return divisors

def solve(n):
    return count_divisors(factorial(n)) % (10**9+7)

if __name__ == '__main__':
    n = int(input())
    print(solve(n))

