
import math

def solve(n, d, r):
    # Calculate the probability of a gem splitting into two gems
    p = 1 / n

    # Calculate the expected number of gems after d nights
    expected_gems = 0
    for i in range(1, n+1):
        expected_gems += i * math.pow(p, d)

    # Calculate the expected number of gems held by the top r inhabitants
    expected_top_r_gems = 0
    for i in range(n-r+1, n+1):
        expected_top_r_gems += i * math.pow(p, d)

    return expected_top_r_gems

