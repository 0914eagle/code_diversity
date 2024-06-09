
import sys

def solve(s, a):
    n = len(s)
    mod = 10**9 + 7
    dp = [[0] * (n+1) for _ in range(27)]
    dp[0][0] = 1
    for i in range(1, 27):
        for j in range(n+1):
            if j-a[i-1] >= 0:
                dp[i][j] = (dp[i][j-a[i-1]] + dp[i-1][j]) % mod
            else:
                dp[i][j] = dp[i-1][j]
    ans = 0
    for i in range(1, 27):
        ans = (ans + dp[i][n]) % mod
    return ans

def longest_substring(s, a):
    n = len(s)
    dp = [0] * 27
    for i in range(n):
        dp[ord(s[i])-ord('a')+1] = max(dp[ord(s[i])-ord('a')+1], i-a[ord(s[i])-ord('a')+1]+1)
    return max(dp)

def min_substrings(s, a):
    n = len(s)
    dp = [0] * 27
    for i in range(n):
        dp[ord(s[i])-ord('a')+1] += 1
    for i in range(1, 27):
        dp[i] = max(dp[i], dp[i-1])
    return dp[26]

s = "aab"
a = [2, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print(solve(s, a))
print(longest_substring(s, a))
print(min_substrings(s, a))

s = "abcdeabcde"
a = [5, 5, 5, 5, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print(solve(s, a))
print(longest_substring(s, a))
print(min_substrings(s, a))

