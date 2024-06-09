
import sys

def get_entirely_unsorted_sequences(arr):
    n = len(arr)
    count = 0
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            temp = arr[:i] + arr[j:]
            if is_sorted(temp):
                count += 1
    return count % (10**9 + 9)

def is_sorted(arr):
    n = len(arr)
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(get_entirely_unsorted_sequences(arr))

