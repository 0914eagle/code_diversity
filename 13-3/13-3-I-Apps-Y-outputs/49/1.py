
def count_good_itineraries(event_types):
    n = len(event_types)
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for j in range(i):
            if event_types[i - 1] != event_types[j]:
                dp[i] += dp[j]
    return dp[n]

