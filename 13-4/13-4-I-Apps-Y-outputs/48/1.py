
import sys

def get_input():
    n, m = map(int, input().split())
    k = [0] * (m + 1)
    s = [[] for _ in range(n + 1)]
    p = [0] * (m + 1)
    for i in range(1, m + 1):
        k[i], *s[i] = map(int, input().split())
        s[i] = set(s[i])
    for i in range(1, m + 1):
        p[i] = int(input())
    return n, m, k, s, p

def solve(n, m, k, s, p):
    dp = [[0] * 2 for _ in range(m + 1)]
    dp[0][0] = 1
    for i in range(1, m + 1):
        for j in range(2):
            for si in s[i]:
                dp[i][j] += dp[si][j ^ 1]
            dp[i][j] %= 1000000007
    ans = 0
    for i in range(1, m + 1):
        if (dp[i][0] + dp[i][1]) % 2 == p[i]:
            ans += 1
    return ans

n, m, k, s, p = get_input()
print(solve(n, m, k, s, p))

