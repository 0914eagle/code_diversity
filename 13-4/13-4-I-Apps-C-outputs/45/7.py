
import math

def solve(n, k):
    n = int(n, 2)
    count = 0
    for i in range(1, n+1):
        num_set_bits = bin(i).count('1')
        if num_set_bits >= k:
            count += 1
    return count % (10**9 + 7)

