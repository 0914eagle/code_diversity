
def solve(N, M, detectors):
    # Initialize a list to store the minimum number of phone calls made between each pair of houses
    min_calls = [[0] * (M + 1) for _ in range(M + 1)]

    # Populate the list with the total number of phone calls detected by each detector
    for detector in detectors:
        pos, calls = detector
        min_calls[pos][pos + 1] = calls
        min_calls[pos + 1][pos] = calls

    # Fill in the rest of the list using the minimum number of phone calls made between each pair of houses
    for i in range(2, M + 1):
        for j in range(i, M + 1):
            min_calls[i][j] = min(min_calls[i - 1][j], min_calls[i][j - 1])

    # Return the minimum number of phone calls made between the first and last house
    return min_calls[1][M]

