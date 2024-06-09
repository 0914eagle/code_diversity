
import sys

def solve(H, W, costs, A):
    # Initialize the dp table with the cost of turning the current digit into 1
    dp = [[costs[A[i][j]] for j in range(W)] for i in range(H)]

    # Loop through each row
    for i in range(H):
        # Loop through each column
        for j in range(W):
            # If the current cell is not -1, we can skip it
            if A[i][j] == -1:
                continue

            # If the current cell is 0, we can turn it into 1 for free
            if A[i][j] == 0:
                dp[i][j] = 0
                continue

            # If the current cell is not 0, we need to find the minimum cost of turning it into 1
            # by considering the costs of turning the previous cells into 1
            min_cost = float('inf')
            for k in range(W):
                # If the previous cell is -1 or the current cell is 0, we can skip it
                if A[i][k] == -1 or A[i][j] == 0:
                    continue

                # Calculate the cost of turning the current cell into 1 by first turning the previous cell into 1
                cost = dp[i][k] + costs[A[i][j] - 1]

                # Update the minimum cost if necessary
                min_cost = min(min_cost, cost)

            # Set the minimum cost for the current cell
            dp[i][j] = min_cost

    # Return the minimum total cost required to turn every digit on the wall into 1
    return min([min(row) for row in dp])

if __name__ == '__main__':
    H, W = map(int, input().split())
    costs = [int(x) for x in input().split()]
    A = [list(map(int, input().split())) for _ in range(H)]
    print(solve(H, W, costs, A))

