
def get_monotonic_renumerations(arr):
    n = len(arr)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(i):
            if arr[i - 1] == arr[j]:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j + 1]
    return dp[n][0]

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(get_monotonic_renumerations(arr) % 998244353)

if __name__ == '__main__':
    main()

