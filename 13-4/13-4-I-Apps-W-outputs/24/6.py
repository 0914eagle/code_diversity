
import sys

def get_contiguous_subsequences(arr, k):
    n = len(arr)
    count = 0
    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += arr[j]
            if curr_sum >= k:
                count += 1
    return count

n, k = map(int, input().split())
arr = list(map(int, input().split()))
print(get_contiguous_subsequences(arr, k))

