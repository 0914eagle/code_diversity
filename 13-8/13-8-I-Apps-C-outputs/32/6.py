
import math

def solve(n, d, r):
    # Calculate the probability of a gem splitting into two gems
    p = 1 / n

    # Calculate the expected number of gems after d nights
    expected_gems = n * (1 - (1 - p) ** d)

    # Calculate the expected number of gems held by the top r inhabitants
    expected_top_r_gems = sum(range(r, n + 1)) * expected_gems / n

    return expected_top_r_gems

