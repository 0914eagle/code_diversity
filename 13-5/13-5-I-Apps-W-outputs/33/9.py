
def get_max_score(values):
    n = len(values)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(i, n + 1):
            if i == j:
                dp[i][j] = 0
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j] + values[i])
    return dp[0][n]

def get_optimal_segment(values):
    n = len(values)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(i, n + 1):
            if i == j:
                dp[i][j] = 0
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j] + values[i])
    optimal_segment = []
    i, j = 0, n
    while i < j:
        if dp[i][j] == dp[i + 1][j]:
            i += 1
        else:
            optimal_segment.append(i)
            j = i
        i += 1
    return optimal_segment

if __name__ == '__main__':
    n = int(input())
    values = list(map(int, input().split()))
    print(get_max_score(values))
    print(get_optimal_segment(values))

