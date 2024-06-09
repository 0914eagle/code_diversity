
MOD = 10**9 + 7

def count_answer_sequences(n, m, hints):
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = 1

    for i in range(1, m + 1):
        l, r, hint = hints[i-1]
        same = hint == "same"
        total = 0
        for j in range(r - l + 2):
            total = (total + dp[i-1][l-1+j]) % MOD
        for j in range(1, n + 1):
            if l <= j <= r:
                dp[i][j] = total - dp[i-1][j-1] if same else dp[i-1][j-1]
            else:
                dp[i][j] = dp[i-1][j-1]

    return sum(dp[m]) % MOD

n, m = map(int, input().split())
hints = []
for _ in range(m):
    l, r, hint = input().split()
    hints.append((int(l), int(r), hint))

print(count_answer_sequences(n, m, hints))
