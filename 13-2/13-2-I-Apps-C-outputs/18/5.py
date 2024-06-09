
import sys

def solve(n, m, hints):
    mod = 1000000007
    dp = [1, 1] + [0] * (n - 1)
    for l, r, same in hints:
        for i in range(l - 1, r):
            if same == "same":
                dp[i] = (dp[i - 1] + dp[i]) % mod
            else:
                dp[i] = (dp[i - 1] - dp[i]) % mod
    return sum(dp) % mod

n, m = map(int, input().split())
hints = []
for _ in range(m):
    l, r, same = input().split()
    hints.append((int(l), int(r), same))
print(solve(n, m, hints))

