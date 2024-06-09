
def solve(numbers, l, s):
    n = len(numbers)
    dp = [0] * (n + 1)
    for i in range(n):
        for j in range(i, -1, -1):
            if numbers[i] - numbers[j] <= s and i - j + 1 >= l:
                dp[i + 1] = max(dp[i + 1], dp[j] + 1)
    return dp[n]

