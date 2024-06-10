
import heapq

def find_minimum_time(n, levels):
    dp = [[float('inf')] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(1, n + 1):
        shortcut_item, shortcut_time, *completion_times = levels[i - 1]
        for j in range(n + 1):
            dp[i][j] = min(dp[i][j], dp[i - 1][j] + completion_times[j])
            if j == shortcut_item:
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + shortcut_time)

    return min(dp[n])

if __name__ == "__main__":
    n = int(input())
    levels = [list(map(int, input().split())) for _ in range(n)]

    print(find_minimum_time(n, levels))
