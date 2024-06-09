
MOD = 10**9 + 7

def count_answer_sequences(n, m, hints):
    dp = [[0] * 2 for _ in range(n + 1)]
    dp[0][0] = 1
    
    for i in range(1, n + 1):
        dp[i][0] = (dp[i - 1][0] + dp[i - 1][1]) % MOD
        dp[i][1] = dp[i - 1][1]
        
        for l, r, hint in hints:
            if i >= l and i <= r:
                if hint == 'same':
                    dp[i][1] = (dp[i][1] + dp[l - 1][0] - dp[i - 1][0] + dp[i - 1][1]) % MOD
                else:
                    dp[i][1] = (dp[i][1] - dp[l - 1][0] + dp[i - 1][0] - dp[i - 1][1]) % MOD
    
    return (dp[n][0] + dp[n][1]) % MOD

n, m = map(int, input().split())
hints = []
for _ in range(m):
    l, r, hint = input().split()
    hints.append((int(l), int(r), hint))

result = count_answer_sequences(n, m, hints)
print(result)
