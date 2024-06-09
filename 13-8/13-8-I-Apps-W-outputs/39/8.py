
import math

def solve(n, m, a, b):
    modulo = 998244353
    powers = [1]
    for i in range(m):
        powers.append(powers[-1] * b[i] % modulo)
    result = 1
    for i in range(n):
        result = (result * (powers[i] - 1 + modulo) % modulo) * (powers[n - i - 1] - 1 + modulo) % modulo
    return result

