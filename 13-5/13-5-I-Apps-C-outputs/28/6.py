
import math

def ways_to_take_exactly_k(n, m, k):
    return math.factorial(n) // (math.factorial(n - k) * math.factorial(k) * m**k) % (10**6 + 7)

