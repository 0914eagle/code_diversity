
def count_regular_sequences(n, s):
    MOD = 10**9 + 7
    m = len(s)
    
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    
    for i in range(1, n + 1):
        for j in range(m + 1):
            for k in range(j, m):
                if s[j:k+1] == s[j:k+1][::-1]:
                    dp[i][k+1] = (dp[i][k+1] + dp[i-1][j]) % MOD
    
    result = sum(dp[n]) % MOD
    return result

n = int(input())
s = input()
print(count_regular_sequences(n, s))
