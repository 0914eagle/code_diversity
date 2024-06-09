
import math

def solve(a, b):
    x = 0
    while True:
        if x * (2 * x + 1) >= a and x * (2 * x - 1) >= b:
            break
        x += 1
    if x * (2 * x + 1) == a and x * (2 * x - 1) == b:
        return x
    else:
        return -1

