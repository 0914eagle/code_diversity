
import sys

def solve(s, a):
    n = len(s)
    mod = 10**9 + 7
    dp = [[0] * (n+1) for _ in range(27)]
    dp[0][0] = 1
    for i in range(1, 27):
        for j in range(n+1):
            if j-a[i-1] >= 0:
                dp[i][j] = (dp[i][j] + dp[i-1][j-a[i-1]]) % mod
            if j-1 >= 0 and s[j-1] == chr(i+96):
                dp[i][j] = (dp[i][j] + dp[i-1][j-1]) % mod
    ways = 0
    max_len = 0
    min_substrings = sys.maxsize
    for i in range(n+1):
        ways = (ways + dp[ord(s[i-1])-96][i]) % mod
        max_len = max(max_len, i)
        min_substrings = min(min_substrings, i)
    return ways, max_len, min_substrings

n = int(input())
s = input()
a = list(map(int, input().split()))
ways, max_len, min_substrings = solve(s, a)
print(ways)
print(max_len)
print(min_substrings)

