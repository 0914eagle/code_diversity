
def get_max_score(a):
    n = len(a)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(i + 1, n + 1):
            dp[i][j] = max(dp[i][j - 1], dp[i + 1][j] + a[i] + a[j - 1])
    return dp[0][n]

def get_optimal_segment(a):
    n = len(a)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(i + 1, n + 1):
            if dp[i][j - 1] > dp[i + 1][j] + a[i] + a[j - 1]:
                dp[i][j] = 1
            else:
                dp[i][j] = 0
    return dp[0][n]

def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(get_max_score(a))
    print(get_optimal_segment(a))

if __name__ == '__main__':
    main()

