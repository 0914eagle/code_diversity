
def solve(N, M, detector_positions, detector_calls):
    # Initialize a list to store the minimum number of calls made between each pair of houses
    min_calls = [[0] * (M + 1) for _ in range(M + 1)]

    # Fill in the values for the first detector
    for i in range(1, M):
        min_calls[i][i + 1] = detector_calls[0]

    # Fill in the values for the remaining detectors
    for i in range(1, N):
        for j in range(1, M):
            min_calls[j][j + 1] = min(min_calls[j][j + 1], detector_calls[i])
            min_calls[j + 1][j] = min(min_calls[j + 1][j], detector_calls[i])

    # Find the minimum number of calls made between any two houses
    min_calls_total = float('inf')
    for i in range(1, M):
        for j in range(i + 1, M + 1):
            min_calls_total = min(min_calls_total, min_calls[i][j])

    return min_calls_total

