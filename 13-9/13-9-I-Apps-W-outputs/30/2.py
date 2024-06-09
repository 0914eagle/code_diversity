
def num_ways_to_choose_subset(scores):
    n = len(scores)
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(n):
        for j in range(i+1):
            if scores[i] >= scores[j]:
                dp[i+1] += dp[j]
    return dp[n]

