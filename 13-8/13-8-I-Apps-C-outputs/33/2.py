
def get_max_points(arr):
    n = len(arr)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + min(arr[i - 1], arr[i - 2]))
    return dp[n]

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(get_max_points(arr))

if __name__ == '__main__':
    main()

