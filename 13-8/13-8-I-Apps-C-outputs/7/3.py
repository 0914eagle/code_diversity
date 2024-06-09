
def max_xor_sum(numbers):
    n = len(numbers)
    dp = [0] * (1 << n)
    for i in range(1, 1 << n):
        for j in range(n):
            if i & (1 << j):
                dp[i] = max(dp[i], dp[i - (1 << j)] ^ numbers[j])
    return dp[(1 << n) - 1]

