
MOD = 1000000007

def count_regular_sequences(n, s):
    m = len(s)
    dp = [[0] * (m + 1) for _ in range(m + 1)]
    dp[0][0] = 1
    
    for i in range(1, m + 1):
        for j in range(m + 1):
            if j > 0:
                dp[i][j] = (dp[i][j] + dp[i-1][j-1]) % MOD
            if j < m:
                dp[i][j] = (dp[i][j] + dp[i-1][j+1]) % MOD
    
    prefix = [0] * (m + 1)
    for i in range(m + 1):
        for j in range(m + 1):
            prefix[i] = (prefix[i] + dp[j][i]) % MOD
    
    result = 0
    for i in range(1, m + 1):
        result = (result + prefix[i]) % MOD
    
    return result

n = int(input())
s = input()
print(count_regular_sequences(n, s))
