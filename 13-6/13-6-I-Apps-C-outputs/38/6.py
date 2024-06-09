
import sys

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def f(a):
    n = len(a)
    values = set()
    for i in range(n):
        for j in range(i+1, n+1):
            values.add(gcd(a[i], *a[i+1:j]))
    return len(values)

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(f(a))

