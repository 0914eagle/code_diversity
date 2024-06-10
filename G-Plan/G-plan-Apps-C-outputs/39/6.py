
def longest_exploration_sequence(n, D, M, arr):
    dp = [1] * n
    max_length = 1

    for i in range(1, n):
        for j in range(i):
            if abs(arr[i] - arr[j]) <= M and i - j <= D:
                dp[i] = max(dp[i], dp[j] + 1)
        max_length = max(max_length, dp[i])

    return max_length

if __name__ == "__main__":
    n, D, M = map(int, input().split())
    arr = list(map(int, input().split()))

    result = longest_exploration_sequence(n, D, M, arr)
    print(result)
