
def solve(arr):
    n = len(arr)
    arr.sort()
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = (dp[i - 1] + i * arr[i - 1]) % 1000000007
    return sum(dp) % 1000000007

