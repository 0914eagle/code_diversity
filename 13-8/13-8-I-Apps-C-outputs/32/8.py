
import math

def gem_island(n, d, r):
    # Calculate the probability of a gem splitting into two
    p = 1 / n

    # Calculate the expected number of gems after d nights
    expected_gems = 0
    for i in range(1, d+1):
        expected_gems += math.comb(n, i) * p ** i * (1 - p) ** (n-i)

    # Calculate the expected number of gems held by the top r inhabitants
    expected_top_r_gems = 0
    for i in range(1, r+1):
        expected_top_r_gems += math.comb(n, i) * p ** i * (1 - p) ** (n-i)

    return expected_top_r_gems

