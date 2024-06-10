
def get_max_points(arr):
    n = len(arr)
    dp = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        dp[i] = max(arr[i], dp[i + 1])
    for i in range(1, n):
        dp[i] = max(dp[i], dp[i - 1] + arr[i])
    return dp[0]

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(get_max_points(arr))

if __name__ == '__main__':
    main()

