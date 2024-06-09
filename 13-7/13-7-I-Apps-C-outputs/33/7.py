
import itertools
import math

def get_average_visitors(n, a, p):
    total = 0
    count = 0
    for perm in itertools.permutations(a):
        curr_sum = 0
        for i in range(n):
            curr_sum += perm[i]
            if curr_sum > p:
                break
        else:
            total += i + 1
            count += 1
    return total / count

