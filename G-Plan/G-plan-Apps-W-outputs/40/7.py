
def calculate_sum_of_partition(a, c):
    n = len(a)
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + a[i]

    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        for j in range(1, c + 1):
            if i - j * c >= 0:
                dp[i] = min(dp[i], dp[i - j * c] + prefix_sum[i] - prefix_sum[i - j * c])

    return dp[n]

if __name__ == "__main__":
    n, c = map(int, input().split())
    a = list(map(int, input().split()))
    result = calculate_sum_of_partition(a, c)
    print(result)
