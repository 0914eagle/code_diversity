
import sys

def get_min_mp(H, W, c, A):
    # Initialize the dp table with the cost of turning the current digit into 1
    dp = [[c[A[i][j]] for j in range(W)] for i in range(H)]

    # Loop through each row and column
    for i in range(H):
        for j in range(W):
            # If the current cell is not a digit, skip it
            if A[i][j] == -1:
                continue

            # If the current cell is a digit, loop through its neighbors
            for k in range(max(0, i-1), min(H, i+2)):
                for l in range(max(0, j-1), min(W, j+2)):
                    # If the neighbor is a digit and has not been visited yet, update the dp table
                    if A[k][l] != -1 and dp[k][l] > dp[i][j] + c[A[i][j]][A[k][l]]:
                        dp[k][l] = dp[i][j] + c[A[i][j]][A[k][l]]

    # Return the minimum total MP required to turn every digit on the wall into 1
    return min(dp[i][j] for i in range(H) for j in range(W) if A[i][j] != -1)

if __name__ == '__main__':
    H, W = map(int, input().split())
    c = [[int(x) for x in input().split()] for _ in range(10)]
    A = [[int(x) for x in input().split()] for _ in range(H)]
    print(get_min_mp(H, W, c, A))

