
import math

def count_special_numbers(n, k):
    count = 0
    for i in range(1, n+1):
        binary = bin(i)[2:]
        count += math.ceil(len(binary) / k)
    return count % (10**9 + 7)

