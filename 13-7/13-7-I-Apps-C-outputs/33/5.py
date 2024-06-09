
import itertools
import math

def get_average_visitors(n, guests, p):
    total = 0
    count = 0
    for order in itertools.permutations(guests):
        visitors = 0
        for i in range(n):
            if sum(order[:i+1]) <= p:
                visitors += 1
            else:
                break
        total += visitors
        count += 1
    return total / count

