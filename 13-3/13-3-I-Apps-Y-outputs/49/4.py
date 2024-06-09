
def count_good_itineraries(event_sequence):
    n = len(event_sequence)
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(1, n + 1):
        for j in range(i):
            if event_sequence[i - 1] != event_sequence[j]:
                dp[i] += dp[j]
    return dp[n]

