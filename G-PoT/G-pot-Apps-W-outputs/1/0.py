
def min_total_noise(N, M, K, buildings):
    freq = [0] * (M + 1)
    noise = [0] * (M + 1)
    dp = [[float('inf')] * (K + 1) for _ in range(M + 1)]
    
    for i in range(1, N + 1):
        freq[buildings[i - 1]] += 1
        noise[buildings[i - 1]] += buildings[i - 1]
        
        for j in range(1, M + 1):
            dp[j][0] = noise[j]
        
        for j in range(1, M + 1):
            for k in range(1, K + 1):
                dp[j][k] = min(dp[j][k], dp[j][k - 1])
                for l in range(1, j):
                    dp[j][k] = min(dp[j][k], dp[l][k - 1] + noise[j])
    
    min_noise = float('inf')
    for j in range(1, M + 1):
        min_noise = min(min_noise, dp[j][K])
    
    return min_noise

# Input parsing
N, M, K = map(int, input().split())
buildings = [int(input()) for _ in range(N)]

result = min_total_noise(N, M, K, buildings)
print(result)
