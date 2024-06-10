
def get_max_value(arr, k):
    n = len(arr)
    dp = [[0] * (n + 1) for _ in range(k + 1)]
    
    for i in range(n):
        dp[0][i] = arr[i]
    
    for i in range(1, k + 1):
        for j in range(i, n + 1):
            dp[i][j] = max(dp[i - 1][k], dp[i][j - 1] + arr[j])
    
    return dp[k][n]

def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(get_max_value(arr, k))

if __name__ == '__main__':
    main()

