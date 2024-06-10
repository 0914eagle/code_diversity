
def get_beauty(arr, k):
    n = len(arr)
    dp = [[0] * (k+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, k+1):
            if i == j:
                dp[i][j] = 0
            elif j == 1:
                dp[i][j] = abs(arr[i-1])
            else:
                dp[i][j] = min(dp[i-1][j-1] + abs(arr[i-1] - arr[i-2]), dp[i-1][j] + abs(arr[i-1]))
    return dp[n][k]

def solve(arr, k):
    n = len(arr)
    beauty = 0
    for i in range(n-k+1):
        beauty += get_beauty(arr[i:i+k], k)
    return beauty % 998244353

if __name__ == '__main__':
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(solve(arr, k))

