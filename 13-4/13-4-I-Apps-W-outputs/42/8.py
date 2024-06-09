
def f1(H, W, C, A):
    # Initialize the dp table with the cost of turning the current digit into 1
    dp = [[C[A[i][j]] for j in range(W)] for i in range(H)]

    # Loop through each row
    for i in range(H):
        # Loop through each column
        for j in range(W):
            # If the current cell is not -1, we can skip it
            if A[i][j] == -1:
                continue
            # Loop through the four neighbors of the current cell
            for k in range(4):
                # Get the neighboring cell's row and column indices
                nr = i + dr[k]
                nc = j + dc[k]
                # If the neighboring cell is within the bounds of the grid and is not -1, we can update the dp table
                if 0 <= nr < H and 0 <= nc < W and A[nr][nc] != -1:
                    dp[i][j] = min(dp[i][j], dp[nr][nc] + C[A[i][j]])

    # Return the minimum total cost to turn every digit on the wall into 1
    return min(dp[i][j] for i in range(H) for j in range(W) if A[i][j] != -1)

def f2(H, W, C, A):
    # Initialize the dp table with the cost of turning the current digit into 1
    dp = [[C[A[i][j]] for j in range(W)] for i in range(H)]

    # Loop through each row
    for i in range(H):
        # Loop through each column
        for j in range(W):
            # If the current cell is not -1, we can skip it
            if A[i][j] == -1:
                continue
            # Loop through the four neighbors of the current cell
            for k in range(4):
                # Get the neighboring cell's row and column indices
                nr = i + dr[k]
                nc = j + dc[k]
                # If the neighboring cell is within the bounds of the grid and is not -1, we can update the dp table
                if 0 <= nr < H and 0 <= nc < W and A[nr][nc] != -1:
                    dp[i][j] = min(dp[i][j], dp[nr][nc] + C[A[i][j]])

    # Return the minimum total cost to turn every digit on the wall into 1
    return min(dp[i][j] for i in range(H) for j in range(W) if A[i][j] != -1)

if __name__ == '__main__':
    H, W = map(int, input().split())
    C = [list(map(int, input().split())) for _ in range(10)]
    A = [list(map(int, input().split())) for _ in range(H)]
    print(f1(H, W, C, A))
    print(f2(H, W, C, A))

