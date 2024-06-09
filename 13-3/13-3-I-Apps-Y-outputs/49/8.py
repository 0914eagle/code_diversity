
def count_good_itineraries(event_sequence):
    n = len(event_sequence)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n + 1):
        for j in range(i):
            if event_sequence[i - 1] != event_sequence[j - 1]:
                dp[i][j] += dp[i - 1][j - 1]
            dp[i][j] += dp[i - 1][j]
    return dp[n][0]

if __name__ == '__main__':
    event_sequence = input()
    print(count_good_itineraries(event_sequence))

