
import math

def number_of_perfect_sets(k):
    count = 0
    for i in range(k+1):
        if i == 0:
            count += 1
        else:
            xor = i
            while xor <= k:
                if xor in range(i+1):
                    count += 1
                xor = xor ^ i
    return count % 1000000007

