
import heapq

def min_time_to_beat_all_levels(n, levels):
    dp = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(1, n + 1):
        for j in range(n + 1):
            dp[i][j] = min(dp[i][j], dp[i - 1][j])
            if j > 0:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + levels[i - 1][j])

    return min(dp[n])

if __name__ == "__main__":
    n = int(input())
    levels = []
    for _ in range(n):
        x, s, *times = map(int, input().split())
        levels.append([float('inf')] + times)
        levels[-1][x] = min(levels[-1][x], s)

    print(min_time_to_beat_all_levels(n, levels))
