
import math

def count_divisors(n):
    count = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            count += 2
    if int(math.sqrt(n)) ** 2 == n:
        count -= 1
    return count

def solve(n):
    return count_divisors(n) % (10**9 + 7)

