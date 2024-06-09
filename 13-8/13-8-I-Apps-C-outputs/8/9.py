
def solve(street, tile_patterns):
    n = len(street)
    m = len(tile_patterns)
    dp = [0] * (n + 1)
    for i in range(m):
        for j in range(n - len(tile_patterns[i]) + 1):
            if street[j:j+len(tile_patterns[i])] == tile_patterns[i]:
                dp[j+len(tile_patterns[i])] = max(dp[j+len(tile_patterns[i])], dp[j]+1)
    return n - dp[n]

