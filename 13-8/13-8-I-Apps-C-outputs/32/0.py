
import math

def gem_split(n, d, r):
    # Calculate the probability of a gem splitting into two gems
    p = 1 / (math.factorial(d) * n**d)

    # Calculate the expected number of gems held by the top r inhabitants
    expected_gems = 0
    for i in range(r):
        expected_gems += (i + 1) * p

    return expected_gems

