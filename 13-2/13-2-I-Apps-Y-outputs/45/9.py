
import math

def get_probability(n):
    return 1 - math.factorial(n) / (math.factorial(n) * n)

n = int(input())
print(get_probability(n))

