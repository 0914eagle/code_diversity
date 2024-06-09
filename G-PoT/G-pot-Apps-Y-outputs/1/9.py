
import math

def calculate_probability(n):
    if n == 1:
        return 0.0
    elif n == 2:
        return 0.5
    else:
        return 1 - math.factorial(n) * sum([((-1)**k) / math.factorial(k) for k in range(n+1)])

N = int(input())
probability = calculate_probability(N)
print("{:.8f}".format(probability))
