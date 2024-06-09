
def min_total_noise(N, M, K, buildings):
    building_counts = [0] * M
    noise_levels = [0] * M
    total_noise = 0
    for building in buildings:
        building_counts[building-1] += 1
        noise_levels[building-1] += building_counts[building-1]
        total_noise += noise_levels[building-1]
    
    dp = [[float('inf')] * (K+1) for _ in range(M+1)]
    dp[0][0] = 0
    
    for i in range(1, M+1):
        for j in range(1, K+1):
            for k in range(i):
                dp[i][j] = min(dp[i][j], dp[k][j-1] + total_noise - noise_levels[i-1] + noise_levels[k])
    
    return min(dp[M])

# Input parsing
N, M, K = map(int, input().split())
buildings = [int(input()) for _ in range(N)]

result = min_total_noise(N, M, K, buildings)
print(result)
