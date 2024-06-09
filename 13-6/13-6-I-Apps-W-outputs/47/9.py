
import math

def solve(n, m):
    probability = 0
    for i in range(1, n+1):
        probability += math.comb(m, i) * math.comb(n, i) / math.comb(n*m, i)
    return probability

