
def get_max_subset(x):
    n = len(x)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                dp[i][j] = 1
            elif x[i - 1] - x[j - 1] == 2 ** dp[i - 1][j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[n][n]

def get_subset(x, dp):
    n = len(x)
    subset = []
    i, j = n, n
    while i > 0 and j > 0:
        if dp[i][j] == dp[i - 1][j]:
            i -= 1
        elif dp[i][j] == dp[i][j - 1]:
            j -= 1
        else:
            subset.append(x[i - 1])
            i -= 1
            j -= 1
    subset.reverse()
    return subset

def main():
    n = int(input())
    x = list(map(int, input().split()))
    dp = get_max_subset(x)
    subset = get_subset(x, dp)
    print(len(subset))
    print(*subset)

if __name__ == '__main__':
    main()

