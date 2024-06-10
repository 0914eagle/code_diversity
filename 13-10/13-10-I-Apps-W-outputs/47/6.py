
def beauty(arr, k):
    n = len(arr)
    dp = [[0] * (k+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, k+1):
            if i == j:
                dp[i][j] = 0
            elif j == 1:
                dp[i][j] = abs(arr[i-1] - arr[i-2])
            else:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i-2][j-1]) + abs(arr[i-1] - arr[i-2])
    return dp[n][k]

def sum_beauty(arr, k):
    n = len(arr)
    dp = [[0] * (k+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, k+1):
            if i == j:
                dp[i][j] = 0
            elif j == 1:
                dp[i][j] = abs(arr[i-1] - arr[i-2])
            else:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i-2][j-1]) + abs(arr[i-1] - arr[i-2])
    return sum(dp[n][1:k+1])

def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(sum_beauty(arr, k))

if __name__ == '__main__':
    main()

