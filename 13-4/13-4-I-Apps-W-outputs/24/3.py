
def solve():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    # Initialize the prefix sum array
    prefix_sum = [0] * (N + 1)
    for i in range(1, N + 1):
        prefix_sum[i] = prefix_sum[i - 1] + A[i - 1]

    # Initialize the count of contiguous subsequences
    count = 0

    # Iterate through the prefix sum array
    for i in range(N):
        # Find the first prefix sum that is greater than or equal to K
        if prefix_sum[i] >= K:
            # Increment the count by 1
            count += 1

    # Return the count of contiguous subsequences
    return count

