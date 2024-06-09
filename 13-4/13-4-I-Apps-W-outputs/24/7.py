
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
    for i in range(N + 1):
        # Find the first index where the prefix sum is greater than or equal to K
        if prefix_sum[i] >= K:
            # Find the last index where the prefix sum is greater than or equal to K
            j = i - 1
            while j >= 0 and prefix_sum[j] >= K:
                j -= 1

            # Add the number of elements in the contiguous subsequence
            count += i - j

    return count

