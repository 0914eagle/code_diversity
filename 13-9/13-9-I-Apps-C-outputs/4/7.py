
import sys

def get_entirely_unsorted_sequences(arr):
    n = len(arr)
    count = 0
    for i in range(1, n + 1):
        for j in range(i):
            for k in range(j):
                if arr[i] < arr[j] and arr[i] < arr[k]:
                    count += 1
    return count % (10**9 + 9)

n = int(input())
arr = list(map(int, input().split()))
print(get_entirely_unsorted_sequences(arr))

