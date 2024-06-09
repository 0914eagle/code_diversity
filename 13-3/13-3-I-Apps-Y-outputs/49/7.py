
def count_good_itineraries(events):
    n = len(events)
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for j in range(i):
            if events[i - 1] != events[j]:
                dp[i] += dp[j]
    return dp[n]

