
import math

def calculate_probability(N):
    if N == 1:
        return 0.0
    else:
        return 1 - math.factorial(N) * (1 - 1/N + 1/(2*math.factorial(N))) / math.factorial(N)

N = int(input())
print("{:.8f}".format(calculate_probability(N)))
