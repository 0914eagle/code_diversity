
import math

def calculate_probability_of_self_gift(N):
    if N == 1:
        return 0.0
    elif N == 2:
        return 0.5
    else:
        return 1 - math.factorial(N) / (N ** N)

N = int(input())
probability = calculate_probability_of_self_gift(N)
print("{:.8f}".format(probability))