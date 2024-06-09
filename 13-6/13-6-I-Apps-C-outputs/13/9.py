
import sys

def f1(n, a):
    # Calculate the number of entirely unsorted sequences
    num_entirely_unsorted = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if a[i] != a[j]:
                num_entirely_unsorted += 1
    return num_entirely_unsorted

def f2(n, a):
    # Calculate the number of entirely unsorted sequences using a more efficient approach
    num_entirely_unsorted = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if a[i] != a[j] and a[i] != a[j - 1]:
                num_entirely_unsorted += 1
    return num_entirely_unsorted

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    print(f1(n, a) % (10**9 + 9))
    print(f2(n, a) % (10**9 + 9))

