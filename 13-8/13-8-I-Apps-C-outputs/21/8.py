
def solve(N, K, board):
    # Initialize a two-dimensional array to store the sums of each domino placement
    sums = [[0] * K for _ in range(N)]

    # Loop through each row of the board
    for i in range(N):
        # Loop through each column of the board
        for j in range(K):
            # Check if the current domino placement is valid
            if j + 1 < K and sums[i][j] < sums[i][j + 1]:
                # Swap the current domino with the next domino
                sums[i][j], sums[i][j + 1] = sums[i][j + 1], sums[i][j]

    # Return the maximum sum possible
    return max(sum(sums[i]) for i in range(N))

