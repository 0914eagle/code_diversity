
import sys

def solve(H, W, costs, A):
    # Initialize the dp table with the cost of turning the current digit into 1
    dp = [[costs[A[i][j]] for j in range(W)] for i in range(H)]

    # Loop through each row and column
    for i in range(H):
        for j in range(W):
            # If the current cell is not a digit, skip it
            if A[i][j] == -1:
                continue

            # If the current cell is the last row and last column, return the cost of turning it into 1
            if i == H-1 and j == W-1:
                return dp[i][j]

            # Get the minimum cost of turning the current cell into 1 by considering all possible previous cells
            min_cost = float('inf')
            for k in range(W):
                if A[i][k] != -1:
                    min_cost = min(min_cost, dp[i][k])
            for k in range(H):
                if A[k][j] != -1:
                    min_cost = min(min_cost, dp[k][j])

            # Update the dp table with the minimum cost
            dp[i][j] += min_cost

    # If the wall is not fully covered, return -1
    return -1

if __name__ == '__main__':
    H, W = map(int, input().split())
    costs = [int(x) for x in input().split()]
    A = [list(map(int, input().split())) for _ in range(H)]
    print(solve(H, W, costs, A))

