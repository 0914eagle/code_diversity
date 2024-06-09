
n = int(input())
s = input()

MOD = 1000000007

def count_regular_sequences(n, s):
    m = len(s)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(1, n + 1):
        for j in range(m + 1):
            for k in range(j, m):
                if s[j:k+1] == s[j:k+1][::-1]:
                    dp[i][k+1] = (dp[i][k+1] + dp[i-1][j]) % MOD

    total_count = sum(dp[n])
    return total_count % MOD

result = count_regular_sequences(n, s)
print(result)
