
def solve(N, K, x):
    # Calculate the minimum distance covered by robots
    min_distance = 0
    for i in range(N):
        if x[i] <= K:
            min_distance += x[i]
        else:
            min_distance += K - x[i] + K
    return min_distance

