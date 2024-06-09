
MOD = 10**9 + 7

def count_answer_sequences(n, m, hints):
    dp = [[0] * 2 for _ in range(n+1)]
    dp[0][0] = 1
    
    for i in range(1, n+1):
        for j in range(2):
            dp[i][j] = dp[i-1][j]
    
    for l, r, hint in hints:
        for i in range(l, r+1):
            if hint == 'same':
                dp[i][1] = (dp[i][1] + dp[l-1][0] - dp[i][0] + MOD) % MOD
            else:
                dp[i][0] = (dp[i][0] + dp[l-1][1] - dp[i][1] + MOD) % MOD
    
    return (dp[n][0] + dp[n][1]) % MOD

n, m = map(int, input().split())
hints = []
for _ in range(m):
    l, r, hint = input().split()
    hints.append((int(l), int(r), hint))

result = count_answer_sequences(n, m, hints)
print(result)
