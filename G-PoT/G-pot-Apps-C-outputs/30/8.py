
MOD = 10**9 + 7

def count_answer_sequences(n, m, hints):
    dp = [[0] * 2 for _ in range(n+1)]
    dp[0][0] = 1
    
    for l, r, hint in hints:
        new_dp = [[0] * 2 for _ in range(n+1)]
        for i in range(n+1):
            new_dp[i][0] = dp[i][0]
            new_dp[i][1] = dp[i][1]
        
        if hint == 'same':
            for i in range(l, r+1):
                new_dp[i][1] += dp[i][0]
                new_dp[i][1] %= MOD
                new_dp[i][0] = 0
        else:
            for i in range(l, r+1):
                new_dp[i][0] += dp[i][1]
                new_dp[i][0] %= MOD
                new_dp[i][1] = 0
        
        dp = new_dp
    
    return (dp[n][0] + dp[n][1]) % MOD

n, m = map(int, input().split())
hints = []
for _ in range(m):
    l, r, hint = input().split()
    hints.append((int(l), int(r), hint))

result = count_answer_sequences(n, m, hints)
print(result)
