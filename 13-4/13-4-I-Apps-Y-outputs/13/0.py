
import sys

def f1(n, a):
    # Calculate the number of different monotonic renumerations of a
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if a[i] == a[j]:
                count += 1
    return count % 998244353

def f2(n, a):
    # Calculate the number of different monotonic renumerations of a
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if a[i] == a[j]:
                count += 1
    return count % 998244353

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(f1(n, a))

