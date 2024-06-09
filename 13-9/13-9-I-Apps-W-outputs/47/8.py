
import sys
import math

sys.setrecursionlimit(10**6)

def prefix_sum(arr):
    n = len(arr)
    prefix_sums = [0] * (n + 1)
    for i in range(n):
        prefix_sums[i + 1] = prefix_sums[i] + arr[i]
    return prefix_sums

def sum_of_subarray_minimums(arr):
    n = len(arr)
    prefix_sums = prefix_sum(arr)
    suffix_sums = prefix_sum(arr[::-1])
    suffix_sums.pop()
    suffix_sums.reverse()
    total_sum = 0
    for i in range(n):
        total_sum += min(prefix_sums[i], suffix_sums[i])
    return total_sum % (10**9 + 7)

def solve(arr):
    n = len(arr)
    total_sum = 0
    for i in range(n):
        for j in range(i, n):
            total_sum += sum_of_subarray_minimums(arr[i:j+1])
    return total_sum % (10**9 + 7)

arr = [int(x) for x in input().split()]
print(solve(arr))

