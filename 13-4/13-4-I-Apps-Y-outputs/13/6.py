
import sys

def f1(n, a):
    # Calculate the number of different monotonic renumerations of a
    count = 0
    for i in range(n):
        count += f2(n, a, i)
    return count % 998244353

def f2(n, a, i):
    # Calculate the number of different monotonic renumerations of a starting from index i
    if i == n-1:
        return 1
    count = 0
    for j in range(i+1, n):
        if a[i] == a[j]:
            count += f2(n, a, j)
        elif a[i] < a[j]:
            count += f2(n, a, j)
    return count

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(f1(n, a))

