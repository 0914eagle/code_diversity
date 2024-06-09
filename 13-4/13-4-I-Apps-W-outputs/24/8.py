
import sys

def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    # Initialize the prefix sum array
    prefix_sum = [0] * (N + 1)
    for i in range(1, N + 1):
        prefix_sum[i] = prefix_sum[i - 1] + A[i - 1]

    # Initialize the answer
    count = 0

    # Iterate through the prefix sum array
    for i in range(N):
        # Find the first index j such that prefix_sum[j] >= K
        j = bisect_left(prefix_sum, K, i, N)

        # If j is not N, then we have found a contiguous subsequence that satisfies the condition
        if j != N:
            count += 1

    return count

def bisect_left(arr, x, lo, hi):
    while lo < hi:
        mid = (lo + hi) // 2
        if arr[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo

if __name__ == '__main__':
    print(solve())

