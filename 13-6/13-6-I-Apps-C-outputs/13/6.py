
import sys

def f1(n, arr):
    # Calculate the number of sorted sequences
    num_sorted = 0
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                num_sorted += 1
    return num_sorted

def f2(n, arr):
    # Calculate the number of unsorted sequences
    num_unsorted = 0
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] != arr[j]:
                num_unsorted += 1
    return num_unsorted

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print((f1(n, arr) * f2(n, arr)) % 1000000009)

