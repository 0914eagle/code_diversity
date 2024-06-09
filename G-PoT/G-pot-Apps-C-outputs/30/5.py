
MOD = 10**9 + 7

def count_answer_sequences(n, m, hints):
    dp = [[0] * 2 for _ in range(n+1)]
    dp[0][0] = 1
    
    for l, r, hint in hints:
        new_dp = [[0] * 2 for _ in range(n+1)]
        
        for i in range(n+1):
            for j in range(i+1):
                if hint == 'same':
                    new_dp[i][j] = (new_dp[i][j] + dp[i][j]) % MOD
                    if j < r:
                        new_dp[r][j+1] = (new_dp[r][j+1] - dp[i][j] + MOD) % MOD
                    if j < l:
                        new_dp[l][j+1] = (new_dp[l][j+1] - dp[i][j] + MOD) % MOD
                else:
                    new_dp[i][j] = (new_dp[i][j] + dp[i][j]) % MOD
                    if j > l:
                        new_dp[l][j-1] = (new_dp[l][j-1] - dp[i][j] + MOD) % MOD
                    if j < r:
                        new_dp[r][j+1] = (new_dp[r][j+1] - dp[i][j] + MOD) % MOD
        
        dp = new_dp
    
    return sum(dp[n]) % MOD

# Read input
n, m = map(int, input().split())
hints = []
for _ in range(m):
    l, r, hint = input().split()
    hints.append((int(l), int(r), hint))

# Calculate and print the answer
print(count_answer_sequences(n, m, hints))
