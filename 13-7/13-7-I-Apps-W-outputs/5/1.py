
def num_surviving_islands(N, T, K, S, V):
    # Initialize a list to keep track of the number of goods received from each island
    goods_received = [0] * (N + 1)
    goods_received[1] = T[1]

    # Iterate through each island and update the number of goods received from other islands
    for i in range(2, N + 1):
        for j in range(K[i - 1]):
            goods_received[i] += V[i - 1][j]
            goods_received[S[i - 1][j]] -= V[i - 1][j]

    # Return the number of islands with enough goods to sustain themselves
    return sum(1 for i in range(1, N + 1) if goods_received[i] >= T[i])

