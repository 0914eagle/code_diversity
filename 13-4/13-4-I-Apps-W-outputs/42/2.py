
def get_cost(c, i, j):
    if i == j:
        return 0
    return c[i, j]

def solve(H, W, C, A):
    # Initialize the dp table with the cost of turning the current digit into 1
    dp = [[get_cost(C, A[i, j], 1) for j in range(W)] for i in range(H)]

    # Loop through each row and column
    for i in range(H):
        for j in range(W):
            # If the current cell is not a digit, skip it
            if A[i, j] == -1:
                continue

            # Loop through the four neighbors of the current cell
            for k in range(4):
                # Get the neighboring cell's row and column indices
                ni = i + (k // 2) - 1
                nj = j + (k % 2) - 1

                # If the neighboring cell is out of bounds, skip it
                if ni < 0 or ni >= H or nj < 0 or nj >= W:
                    continue

                # If the neighboring cell is a digit, update the dp table with the minimum cost
                if A[ni, nj] != -1:
                    dp[i][j] = min(dp[i][j], dp[ni][nj] + get_cost(C, A[i, j], A[ni, nj]))

    # Return the minimum cost to turn all digits on the wall into 1
    return min(dp[i][j] for i in range(H) for j in range(W) if A[i, j] != -1)

def main():
    H, W = map(int, input().split())
    C = [[0] * 10 for _ in range(10)]
    for i in range(10):
        C[i] = list(map(int, input().split()))
    A = [[-1] * W for _ in range(H)]
    for i in range(H):
        A[i] = list(map(int, input().split()))
    print(solve(H, W, C, A))

if __name__ == '__main__':
    main()

