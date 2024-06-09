
import sys

def count_ways(s, a):
    n = len(s)
    mod = 10**9 + 7
    dp = [[0] * (n + 1) for _ in range(27)]
    for i in range(n + 1):
        dp[0][i] = 1
    for i in range(1, 27):
        for j in range(n + 1):
            if j - a[i - 1] >= 0:
                dp[i][j] += dp[i - 1][j - a[i - 1]]
            dp[i][j] %= mod
    return dp[26][n]

def longest_substring(s, a):
    n = len(s)
    dp = [0] * 27
    for i in range(n):
        dp[ord(s[i]) - ord('a') + 1] = max(dp[ord(s[i]) - ord('a') + 1], i - a[ord(s[i]) - ord('a') + 1] + 1)
    return max(dp)

def min_substrings(s, a):
    n = len(s)
    dp = [0] * 27
    for i in range(n):
        dp[ord(s[i]) - ord('a') + 1] += 1
    for i in range(1, 27):
        dp[i] += dp[i - 1]
    return dp[26]

n = int(input())
s = input()
a = list(map(int, input().split()))
print(count_ways(s, a))
print(longest_substring(s, a))
print(min_substrings(s, a))

