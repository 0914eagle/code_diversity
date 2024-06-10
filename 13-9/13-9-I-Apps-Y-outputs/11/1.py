
import math
import sys

def get_input():
    n = int(input())
    a = list(map(int, input().split()))
    return n, a

def get_monotonic_renumeration(a):
    n = len(a)
    b = [0] * n
    b[0] = 0
    for i in range(1, n):
        if a[i] == a[i-1]:
            b[i] = b[i-1]
        else:
            b[i] = b[i-1] + 1
    return b

def count_monotonic_renumerations(a):
    n = len(a)
    b = get_monotonic_renumeration(a)
    count = 1
    for i in range(1, n):
        if b[i] == b[i-1]:
            count *= 2
        else:
            count *= 2 - 1
    return count % (10**9 + 7)

def main():
    n, a = get_input()
    print(count_monotonic_renumerations(a))

if __name__ == '__main__':
    main()

