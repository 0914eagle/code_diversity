
import math

def solve(n, x):
    # Calculate the number of factors of each number
    factors = [0] * (n + 1)
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors[i] += 1
            if i * i != n:
                factors[n // i] += 1
    
    # Calculate the number of ways to stretch the streamers
    ways = 1
    for i in range(n):
        ways *= factors[x[i]]
        ways %= 1000000007
    
    return ways

