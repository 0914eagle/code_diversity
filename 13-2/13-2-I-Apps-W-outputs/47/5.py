
import sys

def solve(s, a):
    n = len(s)
    mod = 10**9 + 7
    dp = [[0] * (n+1) for _ in range(26)]
    dp[0][0] = 1
    for i in range(1, n+1):
        for j in range(26):
            if s[i-1] == chr(j + ord('a')):
                dp[j][i] = (dp[j][i-1] + dp[j-1][i-1]) % mod
            else:
                dp[j][i] = dp[j-1][i-1]
    ways = 0
    max_len = 0
    min_substrings = sys.maxsize
    for i in range(n+1):
        for j in range(26):
            if dp[j][i] > 0:
                ways += dp[j][i]
                max_len = max(max_len, i)
                min_substrings = min(min_substrings, i // a[j])
    return ways % mod, max_len, min_substrings

s = "aab"
a = [2, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print(solve(s, a))

