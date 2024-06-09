
def get_max_product(arr):
    n = len(arr)
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        dp[i] = dp[i - 1] * arr[i - 1]
    for i in range(1, n + 1):
        for j in range(i):
            dp[i] = max(dp[i], dp[j] * dp[i - j])
    return dp[n]

def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(get_max_product(arr))

if __name__ == '__main__':
    main()

