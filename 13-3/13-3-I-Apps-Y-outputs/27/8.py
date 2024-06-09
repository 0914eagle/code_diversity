
import math

def solve(n):
    factorial = math.factorial(n)
    divisors = 0
    for i in range(1, n+1):
        if factorial % i == 0:
            divisors += 1
    return divisors % (10**9+7)

