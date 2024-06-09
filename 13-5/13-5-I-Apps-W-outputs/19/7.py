
def get_max_product(arr):
    n = len(arr)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(i + 1):
            if arr[i] < 0:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + arr[i] * arr[i - 1])
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] - arr[i] * arr[i - 1])
    return dp[n - 1][n]

def solve(arr):
    n = len(arr)
    dp = [0] * n
    for i in range(n):
        if arr[i] < 0:
            dp[i] = -arr[i] - 1
        else:
            dp[i] = arr[i]
    for i in range(n):
        if dp[i] < 0:
            dp[i] = -dp[i] - 1
    return dp

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(*solve(arr))

