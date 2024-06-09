
def min_total_noise_level(N, M, K, buildings):
    building_counts = [0] * M
    total_noise = 0
    for building in buildings:
        building_counts[building - 1] += 1
        total_noise += building_counts[building - 1]
    
    dp = [[float('inf')] * (K + 1) for _ in range(M + 1)]
    dp[0][0] = 0
    
    for i in range(1, M + 1):
        for j in range(1, K + 1):
            for k in range(i):
                dp[i][j] = min(dp[i][j], dp[k][j - 1] + total_noise - sum(building_counts[k:i]))
    
    return min(dp[M])

# Input processing
N, M, K = map(int, input().split())
buildings = [int(input()) for _ in range(N)]

# Call the function and print the result
print(min_total_noise_level(N, M, K, buildings))
