
MOD = 10**9 + 7

def count_answer_sequences(n, m, hints):
    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        for l, r, hint in hints:
            if i >= l and i <= r:
                if hint == 'same':
                    dp[i] = (dp[i] + dp[l - 1]) % MOD
                else:
                    dp[i] = (dp[i] - dp[l - 1] + dp[i]) % MOD

    return dp[n]

n, m = map(int, input().split())
hints = []
for _ in range(m):
    l, r, hint = input().split()
    hints.append((int(l), int(r), hint))

result = count_answer_sequences(n, m, hints)
print(result)
