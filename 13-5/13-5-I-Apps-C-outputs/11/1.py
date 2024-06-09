
import math
import random

def f1(n, x, y, r, b, d):
    # Calculate the probability that the boar hits a tree
    p_hit = 0
    for i in range(n):
        dist = math.sqrt((x - x[i])**2 + (y - y[i])**2)
        if dist < r[i] + b:
            p_hit += 1
    p_hit /= n

    # Calculate the probability that the boar completes its charge without hitting a tree
    p_complete = 1 - p_hit

    return p_complete

def f2(n, x, y, r, b, d):
    # Calculate the probability that the boar hits a tree
    p_hit = 0
    for i in range(n):
        dist = math.sqrt((x - x[i])**2 + (y - y[i])**2)
        if dist < r[i] + b:
            p_hit += 1
    p_hit /= n

    # Calculate the probability that the boar completes its charge without hitting a tree
    p_complete = 1 - p_hit

    return p_complete

if __name__ == '__main__':
    n = int(input())
    x = []
    y = []
    r = []
    for i in range(n):
        xi, yi, ri = map(int, input().split())
        x.append(xi)
        y.append(yi)
        r.append(ri)
    b, d = map(int, input().split())
    print(f1(n, x, y, r, b, d))
    print(f2(n, x, y, r, b, d))

