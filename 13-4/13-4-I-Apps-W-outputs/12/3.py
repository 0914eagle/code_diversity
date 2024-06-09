
def get_max_melody_length(notes):
    n = len(notes)
    dp = [[0] * 2 for _ in range(n)]
    for i in range(n):
        dp[i][0] = 1
        dp[i][1] = 1
        for j in range(i):
            if (notes[i] - notes[j]) % 7 == 1 or notes[i] == notes[j]:
                dp[i][0] = max(dp[i][0], dp[j][0] + 1)
                dp[i][1] = max(dp[i][1], dp[j][1] + 1)
    return max(dp[n-1][0], dp[n-1][1])

