
import sys
import math

def combination(n, k):
    if k > n:
        return 0
    if k == 0:
        return 1
    if k == n:
        return 1
    return combination(n - 1, k - 1) + combination(n - 1, k)

def power(x, y):
    result = 1
    for i in range(y):
        result *= x
    return result

def solve(n, k):
    total = 0
    for i in range(1, n + 1):
        total += combination(n, i) * power(i, k)
    return total % (10**9 + 7)

def main():
    n, k = map(int, input().split())
    print(solve(n, k))

if __name__ == '__main__':
    main()

