
def get_max_score(values):
    n = len(values)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                dp[i][j] = 0
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - 1] + values[j - 1])
    return dp[n][n]

def get_optimal_segment(values):
    n = len(values)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                dp[i][j] = 0
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - 1] + values[j - 1])
    optimal_segment = []
    i, j = n, n
    while i > 0 and j > 0:
        if dp[i][j] == dp[i][j - 1]:
            j -= 1
        else:
            optimal_segment.append(j)
            i -= 1
            j -= 1
    return list(reversed(optimal_segment))

def main():
    n = int(input())
    values = list(map(int, input().split()))
    print(get_max_score(values))
    print(get_optimal_segment(values))

if __name__ == '__main__':
    main()

