
def max_sum(arr, k):
    n = len(arr)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        dp[i][i] = arr[i]
    for i in range(1, n):
        for j in range(0, n - i):
            dp[j][j + i] = max(dp[j][j + i - 1], dp[j + 1][j + i] + arr[j])
    return dp[0][n - 1]

def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(max_sum(arr, k))

if __name__ == '__main__':
    main()

