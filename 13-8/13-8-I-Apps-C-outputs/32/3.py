
import math

def solve(n, d, r):
    # Calculate the probability of a gem splitting into two gems
    p = 1 / n

    # Calculate the expected number of gems held by the top r inhabitants after d nights
    expected_gems = 0
    for i in range(r):
        expected_gems += p * (i + 1)

    return expected_gems

