
def solve(shelves):
    # Initialize variables
    N, M = len(shelves), len(shelves[0])
    K = max(max(row) for row in shelves)
    dp = [[0] * (K + 1) for _ in range(N)]
    for i in range(N):
        for j in range(M):
            dp[i][shelves[i][j]] = 1

    # Fill in the table
    for i in range(N):
        for j in range(M):
            if shelves[i][j] != 0:
                for k in range(1, K + 1):
                    if dp[i][k] == 0 and (j - 1 >= 0 and shelves[i][j - 1] == k or j + 1 < M and shelves[i][j + 1] == k):
                        dp[i][k] = dp[i][shelves[i][j]] + 1

    # Find the minimum number of lifts
    min_lifts = float('inf')
    for i in range(N):
        for j in range(M):
            if shelves[i][j] != 0 and dp[i][shelves[i][j]] < min_lifts:
                min_lifts = dp[i][shelves[i][j]]

    return -1 if min_lifts == float('inf') else min_lifts

