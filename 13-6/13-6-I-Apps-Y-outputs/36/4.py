
def get_maximal_set_of_disjoint_blocks(arr):
    n = len(arr)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                dp[i][j] = 1
            elif arr[i - 1] == arr[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    result = []
    i, j = n, 1
    while i > 0 and j <= n:
        if dp[i][j] == dp[i - 1][j]:
            i -= 1
        elif dp[i][j] == dp[i][j - 1]:
            j += 1
        else:
            result.append((i, j))
            i -= 1
            j += 1
    return result[::-1]

