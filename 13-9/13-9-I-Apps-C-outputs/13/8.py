
import math

def num_special_numbers(n, k):
    count = 0
    for i in range(1, n+1):
        num_ones = bin(i).count('1')
        if num_ones == k:
            count += 1
    return count % (10**9 + 7)

