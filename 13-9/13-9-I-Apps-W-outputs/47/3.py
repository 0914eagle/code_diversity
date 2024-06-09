
def solve(arr):
    n = len(arr)
    mod = 10**9 + 7
    dp = [0] * (n + 1)
    for i in range(n):
        dp[i + 1] = (dp[i] + arr[i] * (i + 1)) % mod
    return sum(dp) % mod

