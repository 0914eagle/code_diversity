
import math

def calculate_probability_of_self_gift(N):
    if N == 1:
        return 0.0
    else:
        return 1.0 - math.factorial(N) / (math.factorial(N) * (N - 1))

N = int(input())
result = calculate_probability_of_self_gift(N)
print("{:.8f}".format(result))
