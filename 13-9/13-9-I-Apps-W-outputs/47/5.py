
import math

def solve(a):
    n = len(a)
    mod = 10**9 + 7
    sum = 0
    for i in range(n):
        for j in range(i, n):
            b = a[i:j+1]
            b.sort()
            sum += (j-i+1) * b[0]
            for k in range(1, len(b)):
                sum += b[k] * (k + i - 1)
            sum %= mod
    return sum

