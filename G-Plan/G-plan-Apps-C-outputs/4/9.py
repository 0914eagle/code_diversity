
import heapq

def min_time_to_beat_all_levels(n, levels):
    dp = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(1, n + 1):
        x, s, *times = levels[i - 1]
        for j in range(n + 1):
            dp[i][j] = min(dp[i][j], dp[i - 1][j] + times[j])
            if j == x:
                dp[i][j] = min(dp[i][j], dp[i - 1][x] + s)

    return min(dp[n])

if __name__ == "__main__":
    n = int(input())
    levels = [list(map(int, input().split())) for _ in range(n)]
    print(min_time_to_beat_all_levels(n, levels))
