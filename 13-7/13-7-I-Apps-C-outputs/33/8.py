
import itertools
import math

def get_average_visitors(n, guests, p):
    total = 0
    count = 0
    for order in itertools.permutations(guests):
        current_sum = 0
        for i in range(n):
            current_sum += order[i]
            if current_sum > p:
                break
        else:
            total += i + 1
            count += 1
    return total / count

